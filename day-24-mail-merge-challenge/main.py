#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
# name_list = []

with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()

print(name_list)
# Replace the [name] placeholder with the actual name.
for name in name_list:
    file_name = "invitation_" + name
    stipped_name = name.strip()
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        with open(f"./Output/ReadyToSend/{file_name}.txt", mode="w") as invitation:
            invitation.write(letter.read().replace("[name]", stipped_name))



#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp