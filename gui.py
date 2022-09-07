import tkinter as tk
from tkinter import TOP, Canvas,Frame,Label
from PIL import ImageTk,Image 
import cv2

window = tk.Tk()

# window properties
window.geometry('1080x1920')
window.title("Beat The Algorithm")
#importing image
imgPathDummy = "images/img.png"
imagPathDummy2 = "images/blue.png"
imagPathDummy3 = "images/main.png"

titleLabel = tk.Label(window, text="BEAT THE ALGORITHM",font=('Arial 20 bold italic'))
titleLabel.pack( padx=20, pady=20)

# comparison frame
comFrame = tk.Frame(window)
comFrame.columnconfigure(0,weight=0)
#comparison canvases
#1
comCanvas1 = Canvas(comFrame, width = 400, height = 300) 
comCanvas1.grid(row=0,column=0)
img1Input= (Image.open(imagPathDummy2))
resized_image11= img1Input.resize((400,300), Image.ANTIALIAS)
blankImage= ImageTk.PhotoImage(resized_image11)
comCanvas1_container = comCanvas1.create_image(10, 10, anchor=tk.NW, image=blankImage) 
#2
comCanvas2 = Canvas(comFrame, width = 400, height = 300) 
comCanvas2.grid(row=1,column=0)
comCanvas2_container = comCanvas2.create_image(10, 10, anchor=tk.NW, image=blankImage) 
#3
comCanvas3 = Canvas(comFrame, width = 400, height = 300) 
comCanvas3.grid(row=2,column=0)
comCanvas1_container = comCanvas3.create_image(10, 10, anchor=tk.NW, image=blankImage) 

comFrame.pack(padx=20, side=tk.RIGHT)

# Attributes frame
attrFrame = tk.Frame(window)
attrFrame.columnconfigure(0)

#pic attributes labels
emoLabel = tk.Label(attrFrame, text="Emotion: N/A",font=('Arial 18'), bd=1, relief= "solid")
emoLabel.grid(row=0,column=0,sticky="W",pady=10)
# titleLabel.pack(side=tk.LEFT, ipadx=10, ipady=10)

secondLabel = tk.Label(attrFrame, text="Smt: N/A",font=('Arial 18'), bd=1, relief= "solid")
secondLabel.grid(row=1,column=0,sticky="W",pady=10)
# titleLabel.pack(side=tk.LEFT,)

attrFrame.pack(anchor = "w", side=TOP,padx=10)

#main canvas
# mainCanvas = Canvas(window, width = 900, height = 700) 
# mainCanvas.pack(padx=(400, 0)) #padx=(250, 0)
# img1Input= (Image.open(imagPathDummy2))
# #Resize the Image using resize method
# resizedMain_image = img1Input.resize((900,700), Image.ANTIALIAS)
# newMain_image= ImageTk.PhotoImage(resizedMain_image)
# mainCanvas_container = mainCanvas.create_image(10, 10, anchor=tk.NW, image=newMain_image) 



# Create a frame
mainFrame = Frame(window, bg="white")
mainFrame.pack()
#Create a label in the frame
mainLabel = Label(mainFrame)
mainLabel.pack()


# # Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    #camera.take_picture()  #this should return a live feed?

    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    mainLabel.imgtk = imgtk
    mainLabel.configure(image=imgtk)
    #mainLabel.after(1, video_stream)  #refresh
    cv2.imwrite("images/picture_" + ".jpg", frame)



def setThreePics(Img1Path,Img2Path,Img3Path):
    #1
    #Resize the Image using resize method
    img1InputFun= (Image.open(Img1Path))
    resized_image1= img1InputFun.resize((400,300), Image.ANTIALIAS)
    new_image1= ImageTk.PhotoImage(resized_image1)
    comCanvas1.itemconfig(comCanvas1_container,image = new_image1)
    comCanvas1.imgref = new_image1
    #2
    img2InputFun= (Image.open(Img2Path))
    resized_image2= img2InputFun.resize((400,300), Image.ANTIALIAS)
    new_image2= ImageTk.PhotoImage(resized_image2)
    comCanvas2.itemconfig(comCanvas1_container,image = new_image2)
    comCanvas2.imgref = new_image2
    # #3
    img3InputFun= (Image.open(Img3Path))
    resized_image3 = img3InputFun.resize((400,300), Image.ANTIALIAS)
    new_image3= ImageTk.PhotoImage(resized_image3)
    comCanvas3.itemconfig(comCanvas1_container,image = new_image3)
    comCanvas3.imgref = new_image3

def setMainFrame(ImgPath):
    imgInputFun= (Image.open(ImgPath))
    resizedMain_image = imgInputFun.resize((900,700), Image.ANTIALIAS)
    newMain_image = ImageTk.PhotoImage(resizedMain_image)
    mainCanvas.itemconfig(mainCanvas_container,image = newMain_image)
    mainCanvas.imgref = newMain_image

def dummpySetImagesAndAttr():
    setMainFrame(imagPathDummy3)
    setThreePics(imgPathDummy,imgPathDummy,imgPathDummy)
    setAttributes("Happy","N/A: N/A")

def reset():
    #set main frame to defult
    img1Input= (Image.open(imagPathDummy2))
    blankImage= ImageTk.PhotoImage(img1Input)
    mainCanvas.itemconfig(mainCanvas_container,image = blankImage)
    mainCanvas.imgref = blankImage
    #set all three pics to defult
    #1
    comCanvas1.itemconfig(comCanvas1_container,image = blankImage)
    comCanvas1.imgref = blankImage
    #2
    comCanvas2.itemconfig(comCanvas1_container,image = blankImage)
    comCanvas2.imgref = blankImage
    #3
    comCanvas3.itemconfig(comCanvas1_container,image = blankImage)
    comCanvas3.imgref = blankImage

    emoLabel['text'] = "Emotion:"
    secondLabel['text'] = "Smt: N/A"

def setAttributes(emotionAttr,secondFullAttr):
    emoLabel['text'] = "Emotion: "+emotionAttr
    secondLabel['text'] = secondFullAttr

# btn frame
btnFrame = tk.Frame(window)
btnFrame.columnconfigure(0,weight=1)
#reset btn
#1
resetBtn = tk.Button(btnFrame, text="RESET", font=('Arial 10'),command=lambda:reset())
resetBtn.grid(row=0,column=0)
#take a pic btn
#2
takePicBtn = tk.Button(btnFrame, text="TAKE A PIC!", font=('Arial 16 bold'),command=lambda:dummpySetImagesAndAttr())
takePicBtn.grid(row=0,column=1)

btnFrame.pack(side=tk.BOTTOM, ipadx=10, ipady=10)

video_stream()
window.mainloop()
