import tkinter
import time
from threading import Timer
from words import words


def get_words():
    wordstyped = speedbox.get()
    wordstypedlist = wordstyped.split()
    numofwordstyped = len(wordstypedlist)
    print(numofwordstyped)


def start_timer():
    speedbox.delete(0, len(speedbox.get()))
    numofwordstyped = 0
    Timer(60, get_words).start()


window = tkinter.Tk()
window.title(
    "Typing speed test"
)
window.config(
)
canvas = tkinter.Canvas(
    highlightthickness=0
)

canvas.grid()

title = tkinter.Label(
    text = "Typing speed test!\n Can you beat 40 words per minute?"

)

title.grid(
    column=2,
    row=0
)
words_to_type = tkinter.Label(
    text=words
)
words_to_type.grid(
     column=2,
     row=1
)
start_button = tkinter.Button(
    text="Start",
    command=start_timer
)
start_button.grid(
    column=1,
    row=2
)
speedbox = tkinter.Entry()
speedbox.grid(
    column=2,
    row=3
)
window.mainloop()