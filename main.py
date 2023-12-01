from tkinter import *
from tkinter import messagebox
import random
import pandas

PINK = "#FF8F8F"
YELLOW = "#EEF296"
DARK_GREEN = "#0b6940"
LIGHT_GREEN = "#9ADE7B"

# UI ------------------------------
window = Tk()
window.title("FlashCard")
window.minsize(width=450, height=610)
window.config(padx=25, pady=25, bg=DARK_GREEN)

canvas = Canvas(width=400, height=266)
word_card_img = PhotoImage(file="images/word_card.png")
meaning_card_img = PhotoImage(file="images/meaning_card.png")
card_current_img = canvas.create_image(200, 133, image=word_card_img)
canvas.config(bg=DARK_GREEN, highlightthickness=0)

card_title = canvas.create_text(190, 50, text="Title:", font=("Arial", 20, "italic"))
card_main_text = canvas.create_text(190, 150, text="The word", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Buttons
i_dont_know_btn = Button(text="I don't know❌", bg=PINK, fg="white", width=16, font=("Arial", 15))
i_dont_know_btn.grid(row=1, column=0)
i_know_btn = Button(text="I know✅", width=16, bg=LIGHT_GREEN, font=("Arial", 15))
i_know_btn.grid(row=1, column=1)

separator_canvas = Canvas(width=400, height=10)
separator_img = PhotoImage(file="images/separator.png")
separator_canvas.create_image(200, 5, image=separator_img)
separator_canvas.config(bg=PINK, highlightthickness=0)
separator_canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=15)

# --------------------------------Insert Section
word_label = Label(text="Word: ")
word_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"))
word_label.grid(row=3, column=0)

meaning_label = Label(text="Meaning: ")
meaning_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"))
meaning_label.grid(row=4, column=0)

part_of_speech_label = Label(text="Past od speech: ")
part_of_speech_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"))
part_of_speech_label.grid(row=5, column=0)

word_entry = Entry(width=32)
word_entry.grid(row=3, column=1)

meaning_textbox = Text(height=4, width=25)
meaning_textbox.grid(row=4, column=1, pady=10)

# ----------------Radio BTNs
radio_state = IntVar()
noun_radio_btn = Radiobutton(text="Noun", value="noun", variable=radio_state)
noun_radio_btn.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "italic"))
noun_radio_btn.grid(row=5, column=1)

verb_radio_btn = Radiobutton(text="Verb", value="verb", variable=radio_state)
verb_radio_btn.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "italic"))
verb_radio_btn.grid(row=6, column=0)

adj_radio_btn = Radiobutton(text="Adjective", value="adjective", variable=radio_state)
adj_radio_btn.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "italic"))
adj_radio_btn.grid(row=6, column=1)

adverb_radio_btn = Radiobutton(text="Adverb", value="adverb", variable=radio_state)
adverb_radio_btn.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "italic"))
adverb_radio_btn.grid(row=7, column=0)

add_btn = Button(text="Add to Dictionary ➡", width=23, fg=DARK_GREEN, bg=YELLOW, font=("Arial", 10))
add_btn.grid(row=7, column=1)

window.mainloop()

# ---------------------- Insert word section
"""
- textbox for word (it shouldn't be empty)
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
