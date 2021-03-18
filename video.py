import cv2

# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
    
cap = cv2.VideoCapture("naruto.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
