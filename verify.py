import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import os
from PIL import Image  
import PIL

# def loop_pictures():
#     path = "images/"
#     images = os.listdir(path)
#     print(images)

#     for img in images:
#         img_arr = cv2.imread(os.path.join(path, img))
#         print(img_arr)   
#     return(img_arr)

def compare_one_to_many(imgPath):
    df = DeepFace.find(img_path=imgPath,
    db_path="images", enforce_detection=False)
    #store image from lastImage to images folder
    img = cv2.imread(imgPath)  
    result = imgPath[imgPath.find('p'):]
    cv2.imwrite("images/"+result, img) 
    # remove image from lastImage
    try:
        os.remove(imgPath) 
    except OSError:
        pass

    return df.head(3)

    # TODO: handle respresnetation_vgg_face.pkl '
    # TODO: calling show images on gui
    #gui.setThreePics()

def getFacialAttribute(imgPath):
    analysis = DeepFace.analyze(img_path = imgPath, actions = ["age", "gender", "emotion", "race"], enforce_detection=False)
    print(analysis)
    return analysis





