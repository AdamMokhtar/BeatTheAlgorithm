# Beat The Algorithm

## How to Run program

Copy the repository with the source code on your machine.

## How to use

## Camera

## GUI

**Need to run:**
```sh
pip install tk 
pip install Pillow
```
### Explanation
This section focuses on creating the interface for the user.
For the development of the GUI TKinter was used which is a Python toolkit.
For the approach of creation, Tkinter Frame was used which helps with grouping and organizing widgets on the GUI.
Following is a breakdown of the important sections of the code:

### Comparison frame
This frame is located on the right-hand side of the screen with one column and three rows. Each row includes a canvas that will hold images.
These images are resized to a specific size to fit the size of the canvas.
 
### Attributes frame
Located on the top left side of the page with one column and two rows.
In each row of these frames, there is a label representing an attribute.
 
 
###  Main Canvas
This canvas is in the center of the page. Which represents the image taken.
 
### Btn frame
This frame is on the center bottom of the screen. The frame has one row and two columns. Each column represents a button. Button RESET which is intended to reset the application. Button TAKE A PIC! Is intended to be used to capture images.
 
### Callable functions
**SetThreePics** 
This function aims to set the three compression images by passing in the three paths of the images which will be set accordingly. Each image passed will be resized to fit the canvas and afterward published.

> Note: change setThreePics to array parameter later!

**setMainFrame**
This method will set the image on the main canvas. As a parameter, the path of the main image will be passed. Further, the image will be resized and published on the main canvas.
 
**setAtrributes**
setAttributes fills in the two labels of the attributes frame.  As the first parameter, a string of the emotion result is expected. while the second parameter expects the label and the result of the second attribute.
 
**rest**
This function resets the images on the comparison frame and the main canvas to the blue blank image.
 
 
**dummpySetImagesAndAttr**
This function sets some dummy data for the images on the comparison frame and the main canvas. Similarly, for the attributes, some dummy data will be filled.



## Model

## Developers

How setup 06-09-2022

In your command line run the command:

`pip3 -r install requirements.txt`
