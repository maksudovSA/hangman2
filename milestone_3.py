#importing word variable from milestone_2
from milestone_2 import word
# Task 1. Step 1: Create a while loop and set the condition to True.
while True:
    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character.
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the guess passes the checks, break out of the loop.
        break
    else:
        # Step 5: If the guess does not pass the checks, print a message.
        print("Invalid letter. Please, enter a single alphabetical character.")

# Print the valid guess
print(f"You guessed: {guess}")

# Task 2. Assuming `word` is the secret word and `guess` is the letter guessed by the user

# Step 1: Create an if statement that checks if the guess is in the word.
if guess in word:
    # Step 2: In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
    print(f"Good guess! {guess} is in the word.")
else:
    # Step 3: Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
    print(f"Sorry, {guess} is not in the word. Try again.")

#Task 3 
def check_guess(guess, word):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()

    # Step 3: Move the code that checks if the guess is in the word into this function.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        # Step 2: Code for checking if input is a valid guess
        guess = input("Enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! That is not a valid input. Please enter a single alphabetical character.")

    # Step 3: Call the check_guess function to check if the guess is in the word.
    check_guess(guess, word)


# Step 4: Call the ask_for_input function to test your code.
ask_for_input()

