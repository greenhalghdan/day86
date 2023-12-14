import tkinter
import time
from threading import Timer
from words import words
import random
import tkinter.messagebox
high_score = "Your current high score is: "
list_of_words = []

def random_words():
    list_of_random_words = random.sample(words, 75)
    return list_of_random_words


def get_words():
    wordstyped = speedbox.get("1.0",tkinter.END)
    wordstypedlist = wordstyped.split()
    i = 0
    correctwords = 0
    global list_of_words
    for word in wordstypedlist:
        if word == list_of_words[i]:
            correctwords += 1
        i += 1
    global High_Score
    High_Score["text"] = f'Your current high score is: {correctwords}'
    tkinter.messagebox.showinfo(message = f'Your current high score is: {correctwords}')


def start_timer():
    global list_of_words
    list_of_words = random_words()
    global word_to_type
    word_to_type.delete("1.0", tkinter.END)
    word_to_type.insert(tkinter.END, list_of_words)
    speedbox.delete("1.0", tkinter.END)
    numofwordstyped = 0
    Timer(20, get_words).start()


window = tkinter.Tk()
window.title(
    "Typing speed test"
)
window.config(
)

title = tkinter.Label(
    text = "Typing speed test!\n Can you beat 40 words per minute?"
)

title.pack(
anchor='center'
)
word_to_type = tkinter.Text(height = 20, width = 52)
word_to_type.insert(tkinter.END, " ")
word_to_type.pack(anchor='center')
start_button = tkinter.Button(
    text="Start",
    command=start_timer
)
High_Score = tkinter.Label(
    text="Your current high score is: "
)
High_Score.pack(
    anchor='center'
)
start_button.pack(
    anchor='center'
)
speedbox = tkinter.Text(height = 20, width = 52)
speedbox.pack(
    anchor='center'
)
window.mainloop()
