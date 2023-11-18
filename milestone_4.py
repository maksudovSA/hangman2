import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialize attributes
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    def check_guess(self, guess):
        # Step 1: Convert the guessed letter to lower case
        guess = guess.lower()

        # Step 2: Create an if statement that checks if the guess is in the word
        if guess in self.word:
            # In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! {guess} is in the word.")
            #Task 3. Define what happens if the letter is in the word.
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        #Task 4. Define wht happens if the letter is not in the word
        else:
            # Step 2: Within the else block
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        # Step 2: Define a method called ask_for_input. In the body of the method, do the following:
        while True:
            guess = input("Enter a single letter (q to quit): ")

            if guess.lower() == 'q':
                print("Quitting the game.")
                exit()

            # Step 2 (continued): Create an if statement that runs if the guess is NOT a single alphabetical character
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            else:
                # Step 2 (continued): Create an elif statement that checks if the guess is already in the list_of_guesses
                if guess in self.list_of_guesses:
                    print(f"You already tried the letter {guess}!")
                else:
                    # Step 2 (continued): If the guess is a single alphabetical character and it's not already in the list_of_guesses,
                    # call the check_guess method. Remember to pass the guess as an argument to this method.
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)  # Append the guess to the list_of_guesses

# # Step 3: Call the ask_for_input method to test your code.
# # Example Usage:
word_list = ["apple", "banana", "cherry", "date", "grapefruit"]
game = Hangman(word_list)
# print(f"Word to guess: {game.word}")
# print(f"Word guessed: {game.word_guessed}")
# print(f"Number of unique letters: {game.num_letters}")
# print(f"Number of lives: {game.num_lives}")
# print(f"List of guesses: {game.list_of_guesses}")
game.ask_for_input()


