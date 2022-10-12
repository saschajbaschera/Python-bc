import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if my_choice >=3 or my_choice <0:
    print("you typed an invalid number, computer wins")
else:
    rps = [rock, paper, scissors]

    print(rps[my_choice] + "\n Computer chose:")

    computer_choice = random.randint(0, 2)

    print(rps[computer_choice])

    if my_choice == computer_choice:
        print("It's a draw")
    elif my_choice == 0 and computer_choice == 1:
        print("Computer wins")
    elif my_choice == 0 and computer_choice == 2:
        print("I win")
    elif computer_choice == 0 and my_choice == 1:
        print("I win")
    elif computer_choice == 0 and my_choice == 2:
        print("Computer wins.")
    elif my_choice == 2 and computer_choice == 1:
        print("I win.")
    elif computer_choice == 2 and my_choice == 1:
        print("Computer wins")

