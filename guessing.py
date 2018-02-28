# James Quintin 28/01/18
# Guessing game adapted from Ian McLoughlin

from random import randint

target = (randint(0, 50))
guess = 51

print("Guess a number between 1 and 50")

while guess != target:
    guess = int(input("Please enter your guess: "))
    if guess == target:
        print("well done, you guessed right!")
    elif guess < target:
        print("Too low")
    else:
        print("Too high")
