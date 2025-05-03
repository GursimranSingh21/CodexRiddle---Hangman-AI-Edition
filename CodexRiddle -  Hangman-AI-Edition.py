import openai
import json
import os
import time

# Initialize OpenAI API key
openai.api_key = "enter-your-api-keey"

# List of words for the game
words = ["apple", "banana", "cherry", "date"]

# Function to load cached riddles (if any)
def load_cached_riddles():
    if os.path.exists("riddles_cache.json"):
        with open("riddles_cache.json", "r") as file:
            return json.load(file)
    return {}

# Function to save riddles to cache
def save_riddles_to_cache(riddles):
    with open("riddles_cache.json", "w") as file:
        json.dump(riddles, file)

# Function to get riddles for multiple words (batch request)
def get_multiple_riddles(words):
    prompt = f"Generate a riddle for each of the following words: {', '.join(words)}"
    
    # Check cache first
    cached_riddles = load_cached_riddles()
    
    # If we have cached riddles for these words, use them
    riddles = {}
    missing_words = []
    for word in words:
        if word in cached_riddles:
            riddles[word] = cached_riddles[word]
        else:
            missing_words.append(word)

    if missing_words:
        # Only make an API call if we have missing words
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",  # or another suitable engine
                prompt=prompt,
                max_tokens=150,  # Adjust this based on your needs
                n=1,
                stop=None,
                temperature=0.7
            )
            
            # Get riddles and add them to the cache
            riddle_text = response.choices[0].text.strip().split("\n")
            for i, word in enumerate(missing_words):
                riddles[word] = riddle_text[i]
            cached_riddles.update(riddles)
            save_riddles_to_cache(cached_riddles)
        except openai.error.OpenAIError as e:
            print(f"API Error: {e}")
            return None
    
    return riddles

# Function to safely call the API with retry logic
def safe_api_call(func, retries=3, delay=2):
    while retries > 0:
        try:
            return func()
        except openai.error.RateLimitError:
            print("Rate limit exceeded, retrying...")
            time.sleep(delay)
            retries -= 1
        except openai.error.OpenAIError as e:
            print(f"API Error: {e}")
            return None
    return None

# Function to get a riddle for a word (with caching)
def get_riddle_for_word(word):
    cached_riddles = load_cached_riddles()
    
    if word in cached_riddles:
        print(f"Using cached riddle for {word}")
        return cached_riddles[word]
    
    # If not cached, call OpenAI API
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # or another engine
            prompt=f"Give me a riddle for the word '{word}'",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        riddle = response.choices[0].text.strip()
        cached_riddles[word] = riddle  # Cache the result
        save_riddles_to_cache(cached_riddles)
        return riddle
    except openai.error.OpenAIError as e:
        print(f"Error: {e}")
        return None

# Function to display word with guessed letters
def display_word(word, guessed_letters):    
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

# Mode selection
mode = input("Enter mode type (player or editor): ").lower()
while mode != "editor" and mode != "player":
    mode = input("Enter mode type (player or editor): ").lower()

if mode == "editor":
    while True:                         
        print("Current list:", words)  
        print("1. Add")                         
        print("2. Change")
        print("3. Delete")
        print("4. Change number of tries")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':                       
            word = input("Enter new word to add: ")
            words.append(word)
            print("Successfully added.")

        elif choice == '2':
            print("Current list:", words)
            change = input("Enter the word to change: ")
            if change in words:
                new_word = input("Enter the new word: ")
                index = words.index(change)
                words[index] = new_word
                print("Element changed successfully.")
            else:
                print("Word not found in the list.")

        elif choice == '3':
            print("Current list:", words)
            delete = input("Enter the word to delete: ")
            if delete in words:
                words.remove(delete)
                print("Element", delete, "deleted successfully.")
            else:
                print("Word not found in the list.")

        elif choice == '4':
            new_tries = int(input("Enter the new number of tries: "))
            if new_tries > 0:
                tries = new_tries
                print("Number of tries changed successfully.")
            else:
                print("Invalid number of tries. Please enter a positive integer.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

elif mode == "player":
    def HANGMAN():
        # Select difficulty
        difficulty_levels = ["easy", "normal", "master", "grandmaster"]
        difficulty = input("Choose difficulty (easy, normal, master, grandmaster): ").lower()
        while difficulty not in difficulty_levels:
            difficulty = input("Invalid choice. Choose difficulty (easy, normal, master, grandmaster): ").lower()

        # Fetch riddles for the word list
        riddles = get_multiple_riddles(words)
        if riddles:
            print(f"Riddle for the game: {riddles}")
        else:
            print("Failed to fetch riddles. Try again later.")

        tries = 6  # Default number of tries
        guessed_letters = []

        print(f"Words in play: {', '.join(words)}")
        
        while tries > 0:
            # Display the word
            for word in words:
                display_word(word, guessed_letters)
            
            guess = input('Enter a letter: ').lower()
            
            if guess in guessed_letters:                
                print('You already guessed that letter.')
                continue
            
            guessed_letters.append(guess)              
            
            for word in words:
                if guess not in word:
                    tries -= 1
                    print(f'Incorrect guess! Tries left: {tries}')

            if all(letter in guessed_letters for word in words for letter in word): 
                print(f'Congratulations! You guessed all the words: {", ".join(words)}')
                break

        if tries == 0:                                  
            print(f'You lost! The words were: {", ".join(words)}')

    HANGMAN()

else:
    print("Invalid mode type. Please choose 'player' or 'editor'.")
