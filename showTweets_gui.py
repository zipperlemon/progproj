from tkinter import *

HEIGHT = 650
WIDTH = 930

root = Tk();
root.configure(bg ="#f7d417")

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bd=0, highlightthickness=0, relief='ridge', bg ="#f7d417")
canvas.pack()

title = Label(root, text="De laatste Tweets", font="SegoeUI 22", fg="#003082", bg="#f7d417")
title.place(relx=0.5, rely=0, anchor='n')

tweet1 = Text(root, font="SegoeUI 16", fg="#003082", bg="#f7d417")
tweet1.insert(INSERT, "Tweet 1 -Floris")
tweet1.place(relx=0.5, rely=0.10, relheight=0.17, relwidth=0.7, anchor='n')

tweet2 = Text(root, font="SegoeUI 16", fg="#003082", bg="#f7d417")
tweet2.insert(INSERT, "Tweet 2 -Floris")
tweet2.place(relx=0.5, rely=0.31, relheight=0.17, relwidth=0.7, anchor='n')

tweet3 = Text(root, font="SegoeUI 16", fg="#003082", bg="#f7d417")
tweet3.insert(INSERT, "Tweet 3 -Floris")
tweet3.place(relx=0.5, rely=0.52, relheight=0.17, relwidth=0.7, anchor='n')

tweet4 = Text(root, font="SegoeUI 16", fg="#003082", bg="#f7d417")
tweet4.insert(INSERT, "Tweet 4 -Floris")
tweet4.place(relx=0.5, rely=0.73, relheight=0.17, relwidth=0.7, anchor='n')

root.mainloop()
