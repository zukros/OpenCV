import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
#height
cap.set(4, 480)
#width
cap.set(10,100)
#brigthnes
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
