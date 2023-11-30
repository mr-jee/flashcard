from tkinter import *
from tkinter import messagebox
import random
import pandas

DARK_PURPLE = "#21094E"
LIGHT_PURPLE = "#511281"
DARK_GREEN = "#4CA1A3"
LIGHT_GREEN = "A5E1AD"

# UI ------------------------------
window = Tk()
window.title("FlashCard")
window.minsize(width=450, height=800)
window.config(padx=25, pady=25, bg=DARK_PURPLE)

canvas = Canvas(width=400, height=266)
word_card_img = PhotoImage(file="images/word_card.png")
meaning_card_img = PhotoImage(file="images/meaning_card.png")
card_current_img = canvas.create_image(200, 133, image=word_card_img)
canvas.config(bg=DARK_PURPLE, highlightthickness=0)

card_title = canvas.create_text(190, 50, text="Title:", font=("Arial", 20, "italic"), fill=LIGHT_PURPLE)
card_main_text = canvas.create_text(190, 150, text="The word", font=("Arial", 40, "bold"), fill=LIGHT_PURPLE)
canvas.grid(row=0, column=0)

# Buttons


window.mainloop()

# ---------------------- Insert word section
"""
- textboxes for word (it shouldn't be empty)
- convert all words to lowercase before saving
- radio buttons for part of speech: noun, verb, adjective, adverb,
    pronoun, preposition, conjunction, interjection
    (it shouldn't be empty)
- a bigger textbox for the meaning (it shouldn't be empty)
- number of remaining correct guess (default is 7)
- check if there was a same word from past, shows the word and the meaning and part of speech
    in message box and ask the if the user wants to replace it
- save the data into a csv file in the name of "english_words.csv"
- search button that look through the english_words.csv and retrieve the details
"""

# ---------------------- Flashcard section
"""
- if there is no english_words.csv it will be created from the Insert word section
- there is 2 buttons which are cross and check so if user doesn't know the meaning presses cross 
    and the card flips, if user know the meaning press check and card flips and reduce 1 from 
    remaining correct guess.
- when remaining correct guess get to 0 , the word will be append to words_learned.csv and
    will be removed from english_word.csv

"""
