from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
abort = False

def ceasar(text_var, shift_var, direction_var):
    cipher_text = ""
    for char in text_var:
        if char not in alphabet:
            cipher_text += char
        else:
            index = alphabet.index(char)
            if index + shift_var > 25:
                index -= 26
            if direction_var == "encode":
                cipher_text += alphabet[index + shift_var]
            if direction_var == "decode":
                cipher_text += alphabet[index - shift_var]
    print(f'The {direction_var}d text is "{cipher_text}"')


while abort == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    
    ceasar(text_var=text, shift_var=shift, direction_var=direction)
    rerun = input("Do you want to go again? Type 'yes' to rerun or 'no' to end the program!\n").lower()

    if rerun == "yes":
        abort = False
    else:
        abort = True
        print("Goodbye pal!")

