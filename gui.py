import tkinter as tk
from tkinter import TOP, Canvas,Frame,Label
from PIL import ImageTk,Image 
import cv2
from datetime import datetime
import os
import verify


window = tk.Tk()

# window properties
window.geometry('1080x1920')
window.title("Beat The Algorithm")
window.configure(bg='blue')
#importing the main image
blankImg = "main.png"
_imagesArr = None


#A Main frame for the camera feed
mainFrame = Frame(window)
mainFrame.rowconfigure(0, weight=4)
mainFrame.rowconfigure(1, weight=3)
mainFrame.columnconfigure(1, weight=4)
mainFrame.columnconfigure(0, weight=3)

# mainFrame.columnconfigure(0, weight=4)
mainFrame.rowconfigure(4, weight=5)


titleLabel = tk.Label(mainFrame, text="BEAT THE ALGORITHM",font=('Arial 20 bold italic'))
titleLabel.grid(row=0,column=1,sticky="N")


#Create a label in the frame
mainLabel = Label(mainFrame)
mainLabel.grid(row=1,column=1,sticky="W")
# mainLabel.pack(anchor=tk.CENTER)

# Capture from camera 
#TODO: Switch index for the external cam
cap = cv2.VideoCapture(0)
_callback_id = None
_frame = None
_lastImgPath = None


# # Attributes frame
attrFrame = tk.Frame(mainFrame)
attrFrame.columnconfigure(0,weight=1)


# #pic attributes labels
emoLabel = tk.Label(attrFrame, text="Emotion:",font=('Arial 18'), bd=1, relief= "solid")
emoLabel.grid(row=0,column=0,sticky="W",padx=5, pady=5)

ageLabel = tk.Label(attrFrame, text="Age:",font=('Arial 18'), bd=1, relief= "solid")
ageLabel.grid(row=1,column=0,sticky="W",padx=5, pady=5)

genderLabel = tk.Label(attrFrame, text="Gender:",font=('Arial 18'), bd=1, relief= "solid")
genderLabel.grid(row=2,column=0,sticky="W",padx=5, pady=5)

raceLabel = tk.Label(attrFrame, text="Race:",font=('Arial 18'), bd=1, relief= "solid")
raceLabel.grid(row=3,column=0,sticky="W",padx=5, pady=5)

attrFrame.grid(row=1,column=2,sticky="W",padx=5, pady=5)
# attrFrame.pack(side=tk.LEFT)




# btn frame
btnFrame = tk.Frame(mainFrame)
#reset btn
#1
resetBtn = tk.Button(btnFrame, text="TAKE A PIC!", font=('Arial 16 bold'),command=lambda:takePic("images"))
resetBtn.grid(row=2,column=0,padx=5, pady=5)
#take a pic btn
#2
takePicBtn = tk.Button(btnFrame, text="TAKE A PIC & FIND ME!", font=('Arial 16 bold'),command=lambda:setImagesAndAttr())
takePicBtn.grid(row=2,column=1,padx=5, pady=5)

# btnFrame.pack(side=tk.BOTTOM, ipadx=10, ipady=10)
btnFrame.grid(row=2,column=1,padx=5, pady=5)

#reset
resetBtn1 = tk.Button(mainFrame, text="RESET", font=('Arial 13'),command=lambda:reset(), bg='red')
resetBtn1.grid(row=4,column=0, rowspan = 5, sticky="SW")


mainFrame.pack(side=tk.LEFT, padx = 250)


# comparison frame
comFrame = tk.Frame(window,bg="white")
comFrame.columnconfigure(0,weight=0)
#comparison canvases
#1
comCanvas1 = Canvas(comFrame, width = 400, height = 300) 
comCanvas1.grid(row=0,column=0)
img1Input= (Image.open(blankImg))
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
comCanvas3_container = comCanvas3.create_image(10, 10, anchor=tk.NW, image=blankImage) 

comFrame.pack(padx=20, side=tk.RIGHT)


# function for video streaming
def video_stream():
    global _callback_id, _frame
    _, _frame = cap.read()
    cv2image = cv2.cvtColor(_frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    mainLabel.imgtk = imgtk
    mainLabel.configure(image=imgtk)
    _callback_id = mainLabel.after(1, video_stream)  #refresh
    

def setThreePics(imagesPaths):
    newImagesPaths = checkDeepfaceOutputPaths(imagesPaths)
    #1
    setImage(newImagesPaths[0],comCanvas1,comCanvas1_container)
    #2
    setImage(newImagesPaths[1],comCanvas2,comCanvas2_container)
    #3
    setImage(newImagesPaths[2],comCanvas3,comCanvas3_container)

def setImage(imgPath, imageCanvas, imageContainer):
    imgInput = (Image.open(imgPath))
    resized_image = imgInput.resize((400,300), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    imageCanvas.itemconfig(imageContainer,image = new_image)
    imageCanvas.imgref = new_image

#this function is to check the three imgs returned and fill in blanck onces if any is empty
def checkDeepfaceOutputPaths(imagesPaths):
    match len(imagesPaths):
        case 3:
            return imagesPaths
        case 2: 
            imagesPaths.append(blankImg)
            return imagesPaths
        case 1: 
            imagesPaths.append(blankImg)
            imagesPaths.append(blankImg)
            return imagesPaths
        case _:
            imagesPaths.append(blankImg)
            imagesPaths.append(blankImg)
            imagesPaths.append(blankImg)
            return imagesPaths

    
def dummpySetImagesAndAttr():
    setThreePics(blankImg,blankImg,blankImg)
    setAttributes("Happy","N/A: N/A")

def takePic(folder):
    global _lastImgPath,_callback_id
    #stope video capture
    mainLabel.after_cancel(_callback_id) 
    curr_datetime = getCurrentDateTime()
    path = folder +"/picture_" + curr_datetime +  ".jpg"
    _lastImgPath = cv2.imwrite(path, _frame) 
    return path

def setImagesAndAttr():
    path =  takePic("lastImage")

    analysis = verify.getFacialAttribute(path)
    setAttributes(analysis["dominant_emotion"],str(analysis["age"]),analysis["gender"],analysis["dominant_race"])
    results = verify.compare_one_to_many(path)
    listResult = results['identity'].to_list()
    setThreePics(listResult)
    
 
    try:
        os.remove("images/representations_vgg_face.pkl") 
    except OSError:
        pass

def getCurrentDateTime():
    return datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    
def reset():
    global _callback_id
    #1
    resetImagesCanvasAndAttributes(blankImage,comCanvas1,comCanvas1_container)
    #2
    resetImagesCanvasAndAttributes(blankImage,comCanvas2,comCanvas2_container)
    #3
    resetImagesCanvasAndAttributes(blankImage,comCanvas3,comCanvas3_container)
    mainLabel.after_cancel(_callback_id) 
    _callback_id = mainLabel.after(1, video_stream)  #refresh

def resetImagesCanvasAndAttributes(imgPath, imageCanvas, imageContainer):
    #set all three pics to default
    imageCanvas.itemconfig(imageContainer,image = blankImage)
    imageCanvas.imgref = imgPath
    #set attributes to default
    emoLabel['text'] = "Emotion:"
    ageLabel['text'] = "Age:"
    genderLabel['text'] ="Gender:"
    raceLabel['text'] ="Race:"



def setAttributes(emotionAttr,ageAttr,genderAttr,raceAttr):
    emoLabel['text'] = "Emotion: " + emotionAttr
    ageLabel['text'] ="Age: "+ ageAttr
    genderLabel['text'] ="Gender: "+ genderAttr
    raceLabel['text'] ="Race: "+ raceAttr



video_stream()

window.mainloop()
