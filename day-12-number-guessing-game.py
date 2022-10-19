import random


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    else:
        return 5

def check_guess(guess, number):
    if guess == number:
        print(f"You guessed the number, congrats, the number was {number}!")
        return True
    elif guess > number:
        print("Too high.\nGuess again.")
        return False
    elif guess < number:
        print("Too low.\nGuess again")
        return False
        
    
def game():
    print("Welcome to the  Number Guessing Game!")
    print("I'm Thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    # print(f"Psst, the number is {number}")
    guessed_number = False
    tries_remaining = set_difficulty()


    while tries_remaining > 0 and guessed_number == False:
        print(f"You have {tries_remaining} attemps remaining to guess the number")
        guess = int(input("Make a guess: "))
        if check_guess(guess, number) == True:
            guessed_number = True
        else:
            tries_remaining -= 1  

    if guessed_number == False and tries_remaining == 0:
        print("You lost, better luck next time")
game()


