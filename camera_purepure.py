# TODO: write unit test https://docs.python.org/3/library/unittest.html
# TODO: write methods
# TODO: Make Class
from re import M
import cv2 as cv
import sys
import os
from datetime import datetime
from deepface import DeepFace


faces = "images"


def similar_face_finder(faces):
    img_database = []
    celebrity_names = []

    def load_images_from_folder(faces):
        for filename in os.listdir(faces):
            celebrity_names.append(filename)
            # TODO: find deepface equavalent of loading images
            # df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
            # https://github.com/serengil/deepface
           # img = face_recognition.load_image_file("faces"/+filename)
            img = DeepFace.find(img_path="images\img1.jpg", db_path=faces)
            if img is not None:
                img_database.append(img)
    load_images_from_folder(faces)


encodings_database = []


def encodings(img_database):
    for i in range(len(img_database)):
        img_encoder = img_database[i]
        # TODO: do with Deepface model equivalent
       # encodingss=face_recognition.face_encodings(img_encoder)[0]
        encodings_database.append(encodings)

    encodings(img_database)
    # TODO: Deepfacemodel equvalent
    me = face_recognition.load_image_file("current.jpg")
    me_encode = face_recognition.face_encodings(me)[0]

    similarity_data = []
    for i in range(len(encodings_database)):
        a = face_recognition.face_distance([me_encode], encodings_database[i])
        similarity_data.append(a)

    most_similar = min(simularity_data)
    index_of_most_similar = similarity_data.index(most_similar)
    img_rgb = cv.cvtColor(
        img_database[index_of_most_similar], cv.COLOR_BGR2RGB)
    img_rgb = cv.resize(img_rgb, (400, 350))
    celebrity_names = celebrity_names[similarity_data.index(most_similar)]
    return img_rgb, celebrity_names


def take_picture():
    face_Cascade = cv.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    dt = datetime.now()

    ts = datetime.timestamp(dt)

    # video camera source (builtin webcam with 0 or 1 with external usb)
    capture = cv.VideoCapture(0)  # capture is instance of VideoCapture Class

    while True:

        retrieval, image = capture.read()
        result = DeepFace.analyze(
            img_path=image,
            actions=['emotion', 'race'],
            enforce_detection=False)

        # convert to grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        faces = face_Cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:

            cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

        emotion = result['dominant_emotion']
        txt = str(emotion)

        cv.putText(image, txt, (100, 100),
                   cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

        cv.imshow("Video", image)

        # check if image is loaded correctly
        if image is None:
            sys.exit("could not open camera")

        # pressing q stops the code
        if cv.waitKey(1) == ord('q'):
            break
        elif cv.waitKey(1) == ord('s'):
            cv.imwrite("images/" + str(ts) + ".jpg", image)
       # elif cv.waitKey(1)== ord('r'):
         #   take_picture()

        #    face = cv.imwrite("images/picture_" + str(ts) + ".jpg", image)
            break
        # return(face)

    capture.release()


# take_picture()
similar_face_finder(faces)
