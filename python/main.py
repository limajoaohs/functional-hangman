from game_logic import (
    select_word,
    create_initial_state,
    get_display_word,
    process_guess,
    get_game_status
)

def display_game_state(game_state):
    print(f"\nPalavra: {get_display_word(game_state)}")
    print(f"Vidas restantes: {game_state['lives']}")
    print(f"Palpites até agora: {', '.join(sorted(game_state['guesses']))}")

def get_user_input():
    return input("Digite seu palpite (uma única letra): ")

def display_game_over_message(status, word):
    if status == "win":
        print(f"\n🎉 Parabéns! Você acertou a palavra: {word}")
    else:
        print(f"\n😥 Fim de Jogo! A palavra era: {word}")

def game_loop(current_state):
    status = get_game_status(current_state)
    if status != "ongoing":
        display_game_over_message(status, current_state["word"])
        return
    display_game_state(current_state)
    guess = get_user_input()
    next_state = process_guess(current_state, guess)
    game_loop(next_state)

if __name__ == "__main__":
    print("--- Bem-vindo ao Jogo da Forca Funcional! ---")
    secret_word = select_word()
    initial_game_state = create_initial_state(secret_word)
    game_loop(initial_game_state)