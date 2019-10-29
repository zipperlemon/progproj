from tkinter import *
import tkinter.messagebox
import os, re


tweetTextList = []

def removeBadChars(string):
    tmp = re.sub("[{}<>]", "", string)
    return tmp


def selectTweetFile(event):
    try:
        tweetsFile = open("tweets/" + tweetList.get(tweetList.curselection()))
        tweets = tweetsFile.read()
        tweetsList = tweets.split(">;")
        for i in range(len(tweetsList)-1):
            tweetSplit = tweetsList[i].split("}.")
            print(len(tweetSplit))
            print(tweetSplit)
            content = tweetSplit[0]
            print(content)
            name = tweetSplit[1]
            print(name)
            tweetTextList.append("{} -{}".format(content, name))

        tweet.delete('1.0', END)
        tweet.insert(INSERT, removeBadChars(tweetTextList[len(tweetTextList)-1]))
    except:
        return False


def denyTweet():
    if len(tweetTextList) > 0:
        tweetTextList.pop()
        tweet.delete('1.0', END)
        print(len(tweetTextList))
        if len(tweetTextList) > 0:
            tweet.insert(INSERT, removeBadChars(tweetTextList[len(tweetTextList) - 1]))


def accTweet:




allTweets = os.listdir("tweets")

HEIGHT = 650
WIDTH = 930

root = Tk();
root.configure(bg ="#f7d417")

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bd=0, highlightthickness=0, relief='ridge', bg ="#f7d417")
canvas.pack()

left_frame = Frame(root)
left_frame.place(relx=0, rely=0, relheight=1)

scrollbar = Scrollbar(left_frame)
scrollbar.pack(side=RIGHT, fill=Y)

tweetList = Listbox(left_frame, yscrollcommand=scrollbar.set, font="SegoeUI 12", selectmode=SINGLE, fg="#003082")
for line in allTweets:
    tweetList.insert(END, line)

tweetList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=tweetList.yview)

tweetList.bind("<<ListboxSelect>>", selectTweetFile)

title = Label(root, text="Keur NS tweets", font="SegoeUI 22", fg="#003082", bg ="#f7d417")
title.place(relx=0.5, rely=0, anchor='n')

tweet = Text(root, font="SegoeUI 22", fg="#003082", bg ="#f7d417", wrap='word')

tweet.place(relx=0.6, rely=0.1, relwidth=0.7, relheight=0.7, anchor='n')

delete = Button(root, text="Weiger", font="SegoeUI 18", bg="#0063d3", fg="#FFF", command=denyTweet)
delete.place(relx=0.25, rely=0.85, relwidth=0.325)

acc = Button(root, text="Accepteer", font="SegoeUI 18", bg="#0063d3", fg="#FFF")
acc.place(relx=0.625, rely=0.85, relwidth=0.325)


root.mainloop()
