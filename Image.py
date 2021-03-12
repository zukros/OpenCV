import cv2

img = cv2.imread("Thor.png")

cv2.imshow("Output", img)
cv2.waitKey(1)


# waitKey(seconds)
# waitKey(0) infinite, captured image will not be terminated until user ends it 
# waitkey(1) 1ms,captured imnage will be terminated after desired sec. 
