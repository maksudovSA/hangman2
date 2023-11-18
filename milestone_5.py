from milestone_4.py import Hangman
word_list = ["apple", "banana", "cherry", "date", "grapefruit"]
game = Hangman(word_list)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
play_game(word_list)
