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


def add_bounding_boxes():
    # add bounding boxes to video stream
    #

    pass


def add_attributes():
    # add emotion
    # add gender
    # add race
    # add
    pass
