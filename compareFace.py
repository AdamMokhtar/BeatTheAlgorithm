# TODO: implement comparision of faces

import cv2 as cv
from deepface import DeepFace

# read image with cv2
cow = cv.imread("images\img2.jpg")
img1 = cv.cvtColor(cow, cv.COLOR_BGR2GRAY)

chicken = cv.imread("images\img1.jpg")
img2 = cv.cvtColor(cow, cv.COLOR_BGR2GRAY)


face_detector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(img2, 1.3, 5)

detected_faces = []

for face in faces:
    x, y, w, h = face
    detected_face = img2[int(y):int(y+h), int(x):int(x+w)]
    detected_faces.append(detected_face)


targets = face_detector.detectMultiScale(img1, 1.3, 5)
x, y, w, h = targets[0]  # this has just a single face
target = img1[int(y):int(y+h), int(x):int(x+w)]

#showing only one image
def compare(img1, img2):
    resp = DeepFace.verify(img1, img2, enforce_detection=False)
    print(resp["verified"])


# for face in detected_face:
#     # compare face and target in each iteration
#     compare(face, target)
