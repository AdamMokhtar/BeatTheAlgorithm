import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace


def verify(img1_path, img2_path):
    img1 = cv2.imread('images\img1.jpg')
    img2 = cv2.imread('images\img2.jpg')

    plt.imshow(img1[:, :, ::-1])
    plt.show()
    plt.imshow(img2[:, :, ::-1])
    plt.show()

    result = DeepFace.verify('images\img1.jpg', 'images\img2.jpg')
    print("result", result)

    verification = result[0]

    if verification:
        print("they are the same")
    else:
        print("they are not same")


verify("img1.jpg", "img2.jpg")
