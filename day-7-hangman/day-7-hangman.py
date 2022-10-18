
import random
from hangman_art import stages, logo
from hangman_words import word_list

#step 1: choose a random word
chosen_word = random.choice(word_list)
print(logo)
# print(f"Psst, your word is {chosen_word}")
#creating the blankspaces for the ui
blankspaces = []

for letters in range(len(chosen_word)):
    blankspaces += "_"

print(f"{' '.join(blankspaces)}")

# #let the user guess a letter
guesses_left = 6

while "_" in blankspaces and guesses_left > 0:
    guessed_letter = input("Guess a letter: ").lower()

    

    if guessed_letter in blankspaces:
              print("You've already guessed this letter!")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter:
            blankspaces[position] = guessed_letter

    if guessed_letter not in chosen_word:
        guesses_left -= 1
        print(f'Unfortunately, "{guessed_letter}" is not in word, you loose a life!')
    
    
    print(f"{' '.join(blankspaces)}")
    print(stages[guesses_left])
            

    if "_" not in blankspaces:
        print("you win")
    elif guesses_left == 0:
        print("you lost")

















# while guesses_left != 0:
#     guessed_letter = input("Guess a letter: ").lower()
#     if guessed_letter in chosen_word_lowered:
#         print("yeah, you got one!")
#     else:
#         print("better luck next time")
#         guesses_left -= 1
#         if guesses_left == 0:
#             print("you lost!")
#     print(guesses_left)
#     print(chosen_word)





#check if the letter is found in the word

#if yes go back to guessin a letter, if not deduct one life

# print(guesses_left)
# print(chosen_word)
# print(chosen_word_lowered)
# print(word_lenght)