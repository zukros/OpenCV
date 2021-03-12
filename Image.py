import cv2
#import

img = cv2.imread("Thor.png")
#mention path of the Image with extensions

cv2.imshow("Output", img)
#name of the window
cv2.waitKey(1)


# waitKey(seconds)
# waitKey(0) infinite, window will not be terminated until user ends it 
# waitkey(1) 1ms, window will be terminated after desired sec. 
