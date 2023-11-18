# Task 1. Step 1: Create a list of 5 favorite fruits
favorite_fruits_list = ["apple", "banana", "cherry", "date", "grapefruit"]

# Step 2: Assign the list to a variable called word_list
word_list = favorite_fruits_list

# Step 3: Print out the newly created list
print(word_list)

# Task2. Step 2: Write import random on the line.
import random

# Step 3: Create the random.choice method and pass the word_list variable into the choice method.
word_list = ["apple", "banana", "cherry", "date", "grapefruit"]
word = random.choice(word_list)

# Step 5: Print out word to the standard output.
print(word)

# Task 3. Step 1: Using the input function, ask the user to enter a single letter.
# Step 2: Assign the input to a variable called guess.
guess = input("Enter a single letter: ")

#Task 4. Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")