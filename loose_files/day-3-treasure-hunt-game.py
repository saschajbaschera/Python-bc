print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choise = input("You are on a mountain and there are two paths, are you going right or left?\n").lower()
if first_choise == "left":
  second_choise = input('You\'re now on the border of a big green lake, do you "wait" or "swim" to an island you think you see?\n').lower()
  if second_choise == "wait":
    third_choise = input('You waited and you were rescued by a mermaid and guided to her secret castle, there you find three doors, which door do you take? "Red", "Blue" or "Yellow"?\n').lower()
    if third_choise == "red":
      print("You're crushed by a pink dragon and you die alone.")
    elif third_choise == "blue":
      print("A gay knight is facing you and decapatates your head with one swing of his penis.")
    elif third_choise == "yellow":
      print("Wow you actually made it, you find the treasure and the treasure is a bag of zweifel chips,       yaay!")
    else:
      print("game over.")
  else:
    print("You are attacked by a goldfish and dragged to the bottom of the green lake where you suffocate to death.")  
else:
  print("You fell of a cliff and your body was crushed")