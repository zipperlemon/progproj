from tkinter import *
import tkinter.messagebox
from datetime import date
import user as us


def maxCharTweet(event):
    """Zorgt dat het maximaal aantal tekens in de tweet niet wordt overschreden"""
    if len(tweetContent.get("1.0", "end-1c")) == 137:
        # Als het maximaal aantal tekens in bereikt mag je alleen nog maar backspce gebruiken
        if event.keysym == "BackSpace":
            tweetContent.configure(state="normal")
        else:
            tweetContent.configure(state="disabled")


def maxCharName(event):
    """Zorgt dat het maximaal aantal tekens in de naam niet wordt overschreden"""
    if len(nameInput.get()) == 136:
        # Als het maximaal aantal tekens in bereikt mag je alleen nog maar backspce gebruiken
        if event.keysym == "BackSpace":
            nameInput.configure(state="normal")
        else:
            nameInput.configure(state="disabled")


def clearName(event):
    """Maakt de naam input leeg"""
    nameInput.delete(0, END)


def saveContent(content, name):
    """Slaat de tweet en de naam op"""
    path = "tweets/"
    try:
        # Slaat de info op in een txt file met als naam de datum van vandaag
        today = date.today().strftime("%d-%m-%y")
        tweets = open(path + today + ".txt", 'a')
        tweets.write("{{{}}}.<{}>;".format(content, name))
        tweets.close()
    except Exception as e:
        print(e)


def checkContent():
    """Checkt de tweet en de naam"""
    content = us.removeBadChars(tweetContent.get("1.0", "end-1c"))
    name = us.removeBadChars(nameInput.get())

    if 0 < len(content) <= 137 and 0 < len(name) <= 136 and len(content) + len(name) <= 137:
        if "naam" in name:
            tkinter.messagebox.showwarning(title="Er ging iets fout", message="Vul een geldige naam in!")
        else:
            nameInput.delete(0, END)
            tweetContent.delete('1.0', END)
            saveContent(content, name)
    else:
        tkinter.messagebox.showwarning(title="Er ging iets fout",
                                       message="De lengte van je tweet of je naam is niet correct!")
        return False


HEIGHT = 550
WIDTH = 700

root = Tk();
root.configure(bg="#f7d417")

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bd=0, highlightthickness=0, relief='ridge', bg="#f7d417")
canvas.pack()

# Titel
title = Label(root, text="Tweet als NS", font="SegoeUI 22", fg="#003082", bg="#f7d417")
title.place(relx=0.50, rely=0, anchor='n')

# De tweet zelf
tweetContent = Text(root, font="SegoeUI 22", wrap='word')
tweetContent.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.5, anchor='n')
tweetContent.bind("<KeyPress>", maxCharTweet)

# De naam input
nameInput = Entry(root, font="Helvetica 22")
# Verwijder die inhoud als er op word gedrukt
nameInput.insert(0, "Vul je naam in")
nameInput.place(relx=0.5, rely=0.715, relwidth=0.75, relheight=0.08, anchor='n')
nameInput.bind("<Button-1>", clearName)
nameInput.bind("<KeyPress>", maxCharName)

# Submit alles
submitButton = Button(root, text="Tweet!", font="SegoeUI 18", bg="#0063d3", fg="#FFF", command=checkContent)
submitButton.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

root.mainloop()
