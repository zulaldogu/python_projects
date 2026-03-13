import random
import art
print(art.logo)

number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

game_over = False
attempt = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

print(f"You have {attempt} attempts remaining to guess the number.")
while attempt > 0 and not game_over:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it. The answer was {guess}")
        game_over = True
    elif guess > number:
        attempt -= 1
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")
    elif guess < number:
        attempt -= 1
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")

if not game_over:
    print("You've run out of guesses, you lose.")
