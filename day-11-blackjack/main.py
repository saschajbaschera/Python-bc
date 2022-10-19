# from replit import clear
from art import logo
import random

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(current_sum):
    new_card = []
    new_card.append(random.choice(cards))
    if new_card[0] == 11 and current_sum >= 11:
        new_card[0] = 1
        return new_card[0]
    else:
        return new_card[0]

def end_game():
    return

def blackjack(computer_cards, user_cards):
    if (sum(computer_cards) == 21 and sum(user_cards) == 21) or sum(computer_cards) == 21:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("Blackjack! computer wins")
        play_the_game()
    elif sum(user_cards) == 21:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("Blackjack, user wins!")
        play_the_game()
    
    
def check_score(computer_cards, user_cards):
    if (sum(user_cards) > 21 and sum(computer_cards) > 21) or (sum(computer_cards) <= 21 and sum(user_cards) > 21):
        print("You went over, You lose")
    elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) <= 21:
        print("Computers card are just better, You lose")
    elif sum(user_cards) <= 21 and sum(user_cards) > sum(computer_cards):
        print("Yayy, you win!")
    elif sum(user_cards) <= 21 and sum(computer_cards) > 21:
        print("Computer went over, You WIN!!")
    elif sum(user_cards) == sum(computer_cards) and sum(user_cards ) < 21:
        print("It's a draw, nobody wins, lame!")


def play_the_game():
    play = input("Do you want to play a round of blackjack? Type 'y' to start or type 'n' to close the app: ")
    if play == "y":
    #   clear()
      print(logo)
      user_cards = []
      computer_cards = []
  
      for _ in range(2):
          user_cards.append(random.choice(cards))
          computer_cards.append(random.choice(cards))
  
      print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
  
      blackjack(computer_cards, user_cards)
      go_again = True
      while sum(user_cards) < 21 and go_again == True:
          next_card = input("Type 'y' to get another card, type 'n' to pass: ")
          if next_card == "y" and go_again == True:
              user_cards.append(draw_card(sum(user_cards)))
              print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
              print(f"Computer's first card: {computer_cards[0]}")
          else:
            go_again = False
      while sum(computer_cards) < 17:
        computer_cards.append(draw_card(sum(computer_cards)))
      print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
      print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
      check_score(computer_cards=computer_cards, user_cards=user_cards)
      play_the_game()
    
                
play_the_game()

