from tkinter import *
from tkinter import messagebox
import random
import pandas as pd

PINK = "#FF8F8F"
YELLOW = "#EEF296"
DARK_GREEN = "#0b6940"
LIGHT_GREEN = "#9ADE7B"


# --------------------------Insert Section Functionality

def is_duplicate(word):
    """ Return True and The duplicate word if a word already exists in the csv file.
    (True/False, word row, index)"""
    try:
        dataframe = pd.read_csv("data/english_words.csv")
    except FileNotFoundError:
        word_df = pd.DataFrame(columns=["word", "meaning", "part_of_speech", "remaining_guess"])
        word_df.to_csv("data/english_words.csv", mode='a', index=False)
        return False, None

    else:
        # print(word in dataframe.word.values)
        return word in dataframe.word.values, dataframe[dataframe.word == word]


def remove_duplicate(index):
    """ Get a word and remove the related row in csv."""
    dataframe = pd.read_csv("data/english_words.csv")
    dataframe = dataframe.drop(labels=index, axis=0)
    dataframe.to_csv("data/english_words.csv", index=False)
    return dataframe


def add_to_db():
    word = word_entry.get().lower().replace(",", "/").strip()
    meaning = meaning_textbox.get("1.0", "end-1c").lower().replace(",", "/").strip()
    part_of_speech = part_of_speech_entry.get().lower().replace(",", "/").strip()
    remaining_guess = 10

    check_duplicate = is_duplicate(word)
    duplicate_word = check_duplicate[1]
    word_dict = {
        "word": word,
        "meaning": meaning,
        "part_of_speech": part_of_speech,
        "remaining_guess": remaining_guess,
    }
    if check_duplicate[0]:
        is_ok = messagebox.askokcancel(title=f"'{word}' already exists!", message="Do you want to replace?")
        if is_ok:
            remove_duplicate(duplicate_word.index)
            word_df = pd.DataFrame([word_dict])
            word_df.to_csv("data/english_words.csv", mode='a', header=False, index=False)
    else:
        word_df = pd.DataFrame([word_dict])
        word_df.to_csv("data/english_words.csv", mode='a', header=False, index=False)
        word_entry.delete(0, END)
        meaning_textbox.delete("1.0", END)
        part_of_speech_entry.delete(0, END)
        messagebox.showinfo(title="SAVED SUCCESSFULLY!✅",
                            message=f"Word: {word.title()}\nPart of speech: {part_of_speech.title()}\nMeaning: {meaning}")


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

card_part_of_speech = canvas.create_text(190, 50, text="Part of speech:", font=("Arial", 20, "italic"))
card_main_text = canvas.create_text(190, 150, text="The word", font=("Arial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Buttons
i_dont_know_btn = Button(text="I don't know❌", bg=PINK, fg="white", width=16, font=("Arial", 15))
i_dont_know_btn.grid(row=1, column=0)
i_know_btn = Button(text="I know✅", width=16, bg=LIGHT_GREEN, font=("Arial", 15))
i_know_btn.grid(row=1, column=1)

separator_canvas = Canvas(width=400, height=3)
separator_img = PhotoImage(file="images/separator.png")
separator_canvas.create_image(200, 5, image=separator_img)
separator_canvas.config(bg=DARK_GREEN, highlightthickness=0)
separator_canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=15)

# --------------------------------Insert Section
word_label = Label(text="Word: ")
word_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"))
word_label.grid(row=3, column=0)

part_of_speech_label = Label(text="Part of speech: ")
part_of_speech_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"), pady=5)
part_of_speech_label.grid(row=4, column=0)

meaning_label = Label(text="Meaning: ")
meaning_label.config(bg=DARK_GREEN, fg="white", font=("Arial", 12, "bold"))
meaning_label.grid(row=5, column=0)

word_entry = Entry(width=32)
word_entry.focus()
word_entry.grid(row=3, column=1)

part_of_speech_entry = Entry(width=32)
part_of_speech_entry.grid(row=4, column=1, pady=5)

meaning_textbox = Text(height=4, width=24)
meaning_textbox.grid(row=5, column=1, pady=10)

add_btn = Button(text="Add to Dictionary ➡", width=36, fg=DARK_GREEN, bg=YELLOW, font=("Arial", 15), command=add_to_db)
add_btn.grid(row=6, column=0, columnspan=2)

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
