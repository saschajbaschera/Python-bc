import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amount_of_names = len(names)

payer = random.randint(0, (amount_of_names - 1))
payer_name = names[payer]

print(f"{payer_name} is going to buy the meal today!")