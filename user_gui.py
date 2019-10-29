from tkinter import *
import tkinter.messagebox, re
from datetime import date


def maxCharTweet(event):
    if len(tweetContent.get("1.0", "end-1c")) == 137:
        if event.keysym == "BackSpace":
            tweetContent.configure(state="normal")
        else:
            tweetContent.configure(state="disabled")
    print(len(str(tweetContent.get("1.0", "end-1c"))))


def maxCharName(event):
    print(len(nameInput.get()))
    if len(nameInput.get()) == 136:
        if event.keysym == "BackSpace":
            nameInput.configure(state="normal")
        else:
            nameInput.configure(state="disabled")


def clearName(event):
    nameInput.delete(0, END)


def saveContent(content, name):
    path = "tweets/"
    try:
        today = date.today().strftime("%d-%m-%y")
        tweets = open(path + today + ".txt", 'a')
        tweets.write("{{{}}}.<{}>;".format(content, name))
    except Exception as e:
        print(e)


def removeBadChars(string):
    tmp = re.sub("[{}<>]", "", string)
    return tmp


def checkContent():
    content = removeBadChars(tweetContent.get("1.0", "end-1c"))
    name = removeBadChars(nameInput.get())

    if 0 < len(content) <= 137 and 0 < len(name) <= 136 and len(content) + len(name) <= 137:
        if "naam" in name:
            tkinter.messagebox.showwarning(title="Er ging iets fout", message="Vul een geldige naam in!")
        else:
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

title = Label(root, text="Tweet als NS", font="SegoeUI 22", fg="#003082", bg="#f7d417")
title.place(relx=0.50, rely=0, anchor='n')

# tweetContent = Entry(root, font="Helvetica 22", justify='center')
# tweetContent.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n')

tweetContent = Text(root, font="SegoeUI 22", wrap='word')
tweetContent.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.5, anchor='n')
tweetContent.bind("<KeyPress>", maxCharTweet)

# lower_frame = Frame(root, bd=10)
# lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

nameInput = Entry(root, font="Helvetica 22")
# onclick delete
nameInput.insert(0, "Vul je naam in")
nameInput.place(relx=0.5, rely=0.715, relwidth=0.75, relheight=0.08, anchor='n')
nameInput.bind("<Button-1>", clearName)
nameInput.bind("<KeyPress>", maxCharName)

submitButton = Button(root, text="Tweet!", font="SegoeUI 18", bg="#0063d3", fg="#FFF", command=checkContent)
submitButton.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

# frame = Frame(root, bg="#80c1ff", bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

# button = Button(frame, text="Test button", font=40)
# button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower_frame = Frame(root, bg="#80c1ff", bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = Label(lower_frame)
# label.place(relwidth=1, relheight=1)

root.mainloop()
