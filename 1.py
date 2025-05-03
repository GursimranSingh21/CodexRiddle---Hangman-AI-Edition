import random
import openai

# OpenAI API key setup (make sure to set your key here)
openai.api_key = "Enter-your-api-key"

# List of predefined words (if GPT fails to generate words)
words = ['apple', 'banana', 'cherry', 'date', 'hello']

# Difficulty level choices
difficulty_levels = ["easy", "normal", "master", "grandmaster"]

# Function to fetch word and riddle from GPT
def get_word_and_riddle(difficulty):
    prompt = ""
    if difficulty == "easy":
        prompt = "Choose a very common word of 3-5 letters and write a simple one-sentence riddle for it."
    elif difficulty == "normal":
        prompt = "Choose a common word of 6-8 letters and write a moderately tricky one-sentence riddle. Include a hint that is not too obvious."
    elif difficulty == "master":
        prompt = "Choose an uncommon word of 8-10 letters and write a clever, multi-layered riddle for it."
    elif difficulty == "grandmaster":
        prompt = "Choose a rare word of 10+ letters and write an abstract, metaphorical riddle that is quite challenging."

    # GPT-3 request for word and riddle generation
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )

    # Extract word and riddle from GPT response
    result = response.choices[0].text.strip()
    word, riddle = result.split(":")  # Assuming output is in format "WORD: riddle"
    return word.strip(), riddle.strip()

# Game mode: editor or player
mode = input("Enter mode type (player or editor):").lower()
while mode != "editor" and mode != "player":
    mode = input("Enter mode type (player or editor):").lower()

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
    def display_word(word, guessed_letters):    
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

    def HANGMAN():
        # Select difficulty
        difficulty = input("Choose difficulty (easy, normal, master, grandmaster): ").lower()
        while difficulty not in difficulty_levels:
            difficulty = input("Invalid choice. Choose difficulty (easy, normal, master, grandmaster): ").lower()

        word, riddle = get_word_and_riddle(difficulty)
        guessed_letters = []                    
        tries = 6                               
        
        print(f"Riddle: {riddle}")
        
        while tries > 0:
            display_word(word, guessed_letters)        
            guess = input('Enter a letter: ').lower()
            
            if guess in guessed_letters:                
                print('You already guessed that letter.')
                continue
            
            guessed_letters.append(guess)              
            if guess in word:                          
                print('Correct guess!')
            else:
                print('Incorrect guess!')
                tries -= 1
                print('Tries left:', tries)

            if all(letter in guessed_letters for letter in word): 
                print(f'Congratulations! You guessed the word: {word}')
                break

        if tries == 0:                                  
            print(f'You lost! The word was: {word}')

    HANGMAN()

else:
    print("Invalid mode type. Please choose 'player' or 'editor'.")
