import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import os


def loop_pictures():
    path = "images/"
    images = os.listdir(path)
    print(images)

    for img in images:
        img_arr = cv2.imread(os.path.join(path, img))
        print(img_arr)
    return (img_arr)


def compare_one_to_many(imgPath):
    df = DeepFace.find(img_path=imgPath,
                       db_path="C:/Users/Alcain/Documents/learning/Adam/BeatTheAlgorithm/images", enforce_detection=False)
    return df.head(3)


def add_bounding_boxes(faces):
    face_cascade = cv2.CascadeClassifier('C:\Users\Alcain\Documents\learning\Adam\BeatTheAlgorithm\haarcascade_frontalface_default.xml')
    # add bounding boxes to video stream
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    """logic on how to add bounding box 
    Take video image recognize face and draw box with (0,0,0) + line thickness"""
    for face in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    emotion = result['dominant_emotion']

    pass


def add_attributes():
    # add emotion
    # add gender
    # add race
    # add
    pass

# add self for oop class stuff


def analyze(frame)
