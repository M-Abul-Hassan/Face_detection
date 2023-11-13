import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test,jpg')
cap = cv2.VideoCapture(0)

while True:
