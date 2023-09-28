from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Variables
current_word = {}

# # Loading the correct csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    word_dict = pandas.DataFrame.to_dict(data, orient="records")


# Functions
def generate_card():
    global title_text, word_text, timer, current_word
    window.after_cancel(timer)
    current_word = random.choice(word_dict)
    canvas.itemconfig(card_image, image=card_front_image)
    fr_word = current_word["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    window.after(3000, show_translation)


def show_translation():
    en_word = current_word["English"]
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_word, fill="white")


def remove_from_list():
    word_dict.remove(current_word)
    df = pandas.DataFrame(word_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_card()


# Window
window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, show_translation)

# Card
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 120, text="", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 250, text="", font=("Arial", 50, "bold"), fill="black")

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=generate_card, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=remove_from_list, bg=BACKGROUND_COLOR, borderwidth=0)
right_button.grid(column=1, row=1)

generate_card()

window.mainloop()
