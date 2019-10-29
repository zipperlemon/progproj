from tkinter import *
import tkinter.messagebox
import os

def selectTweetFile(event):
    print(tweetList.get(tweetList.curselection()))

allTweets = os.listdir("tweets")

HEIGHT = 650
WIDTH = 800

root = Tk();
root.configure(bg ="#f7d417")

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bd=0, highlightthickness=0, relief='ridge', bg ="#f7d417")
canvas.pack()

left_frame = Frame(root)
left_frame.place(relx=0, rely=0, relheight=1)

scrollbar = Scrollbar(left_frame)
scrollbar.pack(side=RIGHT, fill=Y)

tweetList = Listbox(left_frame, yscrollcommand=scrollbar.set, font="SegoeUI 12", selectmode=SINGLE)
for line in allTweets:
    tweetList.insert(END, line)

tweetList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=tweetList.yview)

tweetList.bind("<<ListboxSelect>>", selectTweetFile)

title = Label(root, text="Keur NS tweets", font="SegoeUI 22", fg="#003082", bg ="#f7d417")
title.place(relx=0.50, rely=0, anchor='n')


root.mainloop()