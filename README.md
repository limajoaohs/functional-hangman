Functional Hangman (Python & Clojure)

📖 About The Project

This project is an implementation of the classic Hangman game for the terminal, developed using a strictly functional approach in two different languages: Python and Clojure.

The main goal was to explore and apply fundamental concepts of the functional programming paradigm, such as pure functions, immutability, and the separation of concerns (isolating business logic from I/O side effects).

✨ Features & Concepts

    Pure Game Logic: All game rules (processing a guess, checking for win/loss conditions, etc.) are contained within pure functions with no side effects.

    Immutable State: The game's state is never modified. With every turn, a new state is generated and passed to the next iteration of the main loop.

    I/O Separation: Functions that interact with the terminal (printing to the screen and reading user input) are completely separate from the core game logic.

    Dual Implementation: The same design was applied in two languages to compare how functional principles manifest in a multi-paradigm environment (Python) versus a functional-first environment (Clojure).

🚀 How to Run

To run this project, clone the repository and follow the steps below for the desired version.

Python Version

    Navigate to the python directory:
    Bash

cd python

Run the game using the following command:
Bash

    python3 main.py

Clojure Version

    Make sure you have Babashka installed on your system.

    Navigate to the clojure directory:
    Bash

cd clojure

Run the game using the following command:
Bash

    bb hangman.clj

🛠️ Technologies Used

    Python 3

    Clojure

    Babashka (as a Clojure script interpreter)