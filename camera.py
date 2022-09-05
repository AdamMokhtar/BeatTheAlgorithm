# TODO: write unit test https://docs.python.org/3/library/unittest.html
# TODO: write methods
# TODO: Make Class
import cv2 as cv
import sys
from datetime import datetime
from deepface import DeepFace


def take_picture():
    face_Cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
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
            cv.imwrite("images/picture_" + str(ts) + ".jpg", image)
       # elif cv.waitKey(1)== ord('r'):
         #   take_picture()

        #    face = cv.imwrite("images/picture_" + str(ts) + ".jpg", image)
            break
        # return(face)
    capture.release()


take_picture()
