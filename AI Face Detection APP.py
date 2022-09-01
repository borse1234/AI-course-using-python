import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontal_default.xml')

# Choose as image to detect faces in
img = cv2.imread('Robert-Downey-Jr.png')


cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()

print("Code Completed")