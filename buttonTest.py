import tkinter as tk
from time import time, sleep

window = tk.Tk()
window.geometry('70x70')
window.title("Beat The Algorithm")


go = False



def showJudgments(self, event=None):
    global go
    if go == False:
        go = True
        showJudgmentsA()
        sleep(5)
    else: 
        keepShowing()
        
def keepShowing():
    global go
    print('a key being pressed')
    go = False

def makeChoice(self, event=None):
    print("makeChoice")

def showJudgmentsA():
    global go
    print("showJudgmentsA")


window.bind('<a>', showJudgments)
window.bind('<KeyRelease-a>', makeChoice)



window.mainloop()