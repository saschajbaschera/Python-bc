# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

other_bidders = True
bidders = {}

def calculation():
  winner_name = ""
  winner_amount = 0
  
  for entries in bidders:
    value = bidders[entries]
    if value > winner_amount:
      winner_name = entries
      winner_amount = bidders[entries]

  print(f"The winner is {winner_name} with a bid of ${winner_amount}.")

while other_bidders == True:
  bidder_name = input("What is your name?\n")
  bidder_amount = int(input("What's your bid?\n$"))

  bidders[bidder_name] = bidder_amount
  more = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if more == "no":
    other_bidders = False
  elif more == "yes":
    # clear()
    print("There you go")

calculation()




