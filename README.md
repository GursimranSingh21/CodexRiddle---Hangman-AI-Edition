# CodexRiddle - Hangman-AI-Edition (Word Management & AI Riddle Integration)
CodexRiddle is an AI-integrated Hangman game built with Python, a new version of the Python Hangman game project. It uses OpenAI's GPT API to generate riddles, features player and editor modes, and includes local caching for performance. A strong showcase of API integration, game logic, and modular programming

🔹 General Overview

This is a Python-based Hangman game that combines traditional word-guessing gameplay with the power of AI-generated riddles using OpenAI's GPT model. It offers two interactive modes:
•	Player Mode – Play classic Hangman, but with a twist: guess the word based on a riddle clue.
•	Editor Mode – Manage the word list and game settings (like number of tries) interactively.
Built for both fun and flexibility, the game supports multiple difficulty levels, custom word management, and local caching of riddles to minimize API usage. It's ideal for programmers looking to combine Python fundamentals with modern AI integrations.
________________________________________
📘 Detailed Breakdown
🎮 Features
🔹 Player Mode
•	Play a game of Hangman with riddle-based hints.
•	Difficulty levels: easy, normal, master, and grandmaster.
•	One-letter guessing system with tracking of guessed letters and remaining tries.
•	Win by revealing all letters before your tries run out.
🔹 Editor Mode (Word Management)
•	Add new words to the word list. (Feature from the classic version.)
•	Change or delete existing words.
•	Set the number of tries allowed in player mode.
________________________________________
💻 Requirements
•	Python 3.6 or higher.
•	OpenAI API Key for generating riddles.
•	Internet connection for first-time riddle generation.
Installation: (cmd ) <your-python-directory> -m pip install openai
________________________________________
⚙️ Setup Instructions
1.	Clone the repository or download the project files.
2.	Ensure Python 3.6+ is installed on your machine.
3.	Install dependencies (e.g., OpenAI package).
4.	Get your API key from OpenAI and replace "your-api-key" in the script.
________________________________________
🚀 How to Use
🧭 Mode Selection
•	Editor Mode: Manage words and change settings.
•	Player Mode: Start playing the game with AI-generated riddles.
🛠 Editor Mode Options
1.	Add – Add a new word to the list.
2.	Change – Replace an existing word with a new one.
3.	Delete – Remove a word from the list.
4.	Change number of tries – Modify how many incorrect guesses are allowed.
5.	Quit – Exit the editor.
🕹 Player Mode Flow
•	Select difficulty.
•	Receive a riddle (from cache or OpenAI).
•	Guess letters to uncover the word.
•	Win by guessing all letters, or lose after all tries are used.
________________________________________
🤖 API & Riddle Caching
AI Riddle Generation
•	Uses OpenAI's GPT model to create custom riddles based on selected words.
Caching System
•	Generated riddles are stored in a local file (riddles_cache.json).
•	If a riddle for a word exists, it's reused—reducing API calls and improving speed.
________________________________________
❗ Troubleshooting
•	Rate Limit Issues: The game includes retry logic. If you exceed your quota, check your OpenAI billing/settings.
•	No Riddle Appears: Ensure your internet connection is stable and the API key is valid.
•	Dependencies Missing: Re-run installation for OpenAI.
________________________________________
📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with minimal
