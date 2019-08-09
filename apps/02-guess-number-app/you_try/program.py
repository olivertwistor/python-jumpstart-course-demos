# Program file for Guess that number game.
import random

print("----------------------")
print("Guess that number game")
print("----------------------")

# Define range of the random number and roll the actual number,
range_low = 0
range_high = 100
random_number = random.randint(range_low, range_high)

# Initialize the guess to an impossible number.
guess = range_high + 1

while guess != random_number:

    user_input = input("Please guess a number between {} and {} (both inclusively): ".format(range_low, range_high))
    guess = int(user_input)

    if guess < random_number:
        print("Sorry, your guess of {} was too LOW.".format(guess))
    elif guess > random_number:
        print("Sorry, your guess of {} was too HIGH.".format(guess))
    else:
        print("Your guess was correct. Well done!")
