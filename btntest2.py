import time
import tkinter as tk

root = tk.Tk()

def key_handler(event=None):
    if event and event.keysym in ('a'):
        print("!!!!!! -> first  do function")
    

# def showJudgments(self, event=None):
#     print("!!!!!! -> first  do function")

# root.bind('<a>', showJudgments)
#root.bind("<1>", lambda event: root.focus_set())
root.bind("<KeyRelease>", key_handler)
root.mainloop()

