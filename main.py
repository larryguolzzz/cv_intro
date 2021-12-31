import cv2
import numpy as np
print("Import successful")


#1. Read images
def readImg():
    img = cv2.imread('lena.png')
    cv2.imshow('image', img)
    cv2.waitKey(0)

#2. Read videos
def openCam():

    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#3. Modify image
def modImg():
    img = cv2.imread('lena.png')
    kernel = np.ones((5,5),np.uint8)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(img,150,200)
    dialate = cv2.dilate(canny,kernel,iterations=1)
    erode = cv2.erode(dialate,kernel,iterations=1)

    cv2.imshow('Gray image', gray)
    cv2.imshow('Blur image', blur)
    cv2.imshow('Canny image', canny)
    cv2.imshow('Dialated image', dialate)
    cv2.imshow('Eroded image', erode)
    cv2.waitKey(0)

#4. Resize image
def resizeImg():
    img = cv2.imread('lena.png')
    print(img.shape)

    resized = cv2.resize(img,(300,300))
    print(resized.shape)

    crop = img[0:200,200:500]

    cv2.imshow('image',img)
    cv2.imshow('Resized image', resized)
    cv2.imshow('Cropped image',crop)
    cv2.waitKey(0)

#5. Draw
def draw():
    img = np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
    cv2.rectangle(img,(0,0),(200,300),(255,0,0),3)
    cv2.circle(img,(300,100),50,(255,0,0),3)
    cv2.putText(img,'Hello world',(200,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),5)
    cv2.imshow('image',img)
    cv2.waitKey(0)


#6. stack images
def stackImg():
    img = cv2.imread('lena.png')
    imgHor = np.hstack((img,img))
    imgVert = np.vstack((img,img))
    cv2.imshow('Horizontal', imgHor)
    cv2.imshow('Vertical', imgVert)
    cv2.waitKey(0)

#7. findCont
def findCont():
    img = cv2.imread('shape.jpeg')
    img_cont = img.copy()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),1)
    canny = cv2.Canny(blur,50,100)

    cont, hir = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for ct in cont:
        area = cv2.contourArea(ct)
        print(area)
        cv2.drawContours(img_cont,ct,-1,(255,0,0),3)

    cv2.imshow('image', img)
    cv2.imshow('contour', img_cont)

    cv2.waitKey(0)
