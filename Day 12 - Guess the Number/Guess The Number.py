from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
easy_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if easy_hard == "easy":
    attempts = 10
elif easy_hard == "hard":
    attempts = 5

win = False
number = random.randint(1, 100)

while attempts != 0 and not win:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_number = int(input("Make a guess: "))
    if user_number > number:
        print("Too high")
        attempts -= 1
    elif user_number < number:
        print("Too low")
        attempts -= 1
    elif user_number == number:
        print(f"You got it! The answer was {user_number}")
        win = True

if not win:
    print(f"You lose. The answer was {number}")