import random
from art import logo

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    number = random.randint(1, 100)
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"You've run out of guesses. The number was {number}.")

number_guessing_game()