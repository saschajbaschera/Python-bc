import random
from game_data import data
from art import logo, vs

#create a function to select a random contester and return it
def random_contester():
    contester = {}
    contester = random.choice(data)
    return contester

#write a function to Compare A and B follower, and return if true or fals 
def compare(follower_a, follower_b, guess):
    if guess == "a":
        if follower_a > follower_b:
            return True
        else:
            return False
    if guess == "b":
        if follower_b > follower_a:
            return True
        else:
            return False

def game():
    game_running = True
    score = 0
    #assign a random contester to contester_A
    contester_a = {}
    if contester_a == {}:
        contester_a = random_contester()

    while game_running == True:
        #display logo // SKIP
        print(logo)
        #Print score
        
        if score > 0:
            print(f"You're right! Current score: {score}")
     
        #show name, discription and the country of A
        print(f'Compare A: {contester_a["name"]}, a {contester_a["description"]}, from {contester_a["country"]}')

        #show vs ascii symbol // SKIP
        print(vs)

        #Choose a random opponent from the game data set and set as B
        contester_b = random_contester()

        #Make sure it's not the same as A
        while contester_a == contester_b:
            contester_b = random_contester()

        #Print contester b
        print(f'Against B: {contester_b["name"]}, a {contester_b["description"]}, from {contester_b["country"]}')

        #Ask who has more followers A or B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #write a function to Compare A and B follower, and return if true or false
        result = compare(contester_a["follower_count"], contester_b["follower_count"], guess)
        # if guess was True, add one to the score
        if result == True:
            score += 1
            if guess == "b":
                contester_a = contester_b
        else:
            #If guess was False, game over and show final score and terminate app.
            game_running = False
            print(logo)
            print(f"Sorry, that's wrong, Final score: {score}")
            return

game()
    
    


