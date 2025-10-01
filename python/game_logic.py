import random

WORD_LIST = [
    "COMPUTADOR", "PROGRAMACAO", "ALGORITMO", "BIBLIOTECA", "PARADIGMA",
    "LINGUAGEM", "VARIAVEL", "CONSTANTE", "FRAMEWORK", "DESENVOLVEDOR",
    "ELEFANTE", "GIRAFA", "HIPOPOTAMO", "CACHORRO", "GATO", "PASSARINHO",
    "BORBOLETA", "ABACAXI", "MELANCIA", "MORANGO", "LARANJA", "BANANA",
    "UNIVERSIDADE", "CONHECIMENTO", "ESTUDANTE", "PROFESSOR", "DISCIPLINA"
]

def select_word(seed=None):
    if seed:
        random.seed(seed)
    return random.choice(WORD_LIST)

def create_initial_state(word, max_lives=6):
    return {
        "word": word,
        "guesses": frozenset(),
        "lives": max_lives,
    }

def get_display_word(game_state):
    word = game_state["word"]
    guesses = game_state["guesses"]
    return " ".join([char if char in guesses else "_" for char in word])

def process_guess(game_state, guess):
    guess = guess.upper()
    if len(guess) != 1 or not guess.isalpha() or guess in game_state["guesses"]:
        return game_state
    new_guesses = game_state["guesses"] | {guess}
    if guess in game_state["word"]:
        return {**game_state, "guesses": new_guesses}
    else:
        return {**game_state, "guesses": new_guesses, "lives": game_state["lives"] - 1}

def get_game_status(game_state):
    word = game_state["word"]
    guesses = game_state["guesses"]
    lives = game_state["lives"]
    if lives <= 0:
        return "loss"
    if all(char in guesses for char in word):
        return "win"
    return "ongoing"