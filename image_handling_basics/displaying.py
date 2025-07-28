import cv2

img = cv2.imread('images/1.png')

if img is not None:
    cv2.imshow("This is image", img) # show the image
    cv2.waitKey(0) # wait for key press to close 
    cv2.destroyAllWindows() #close the window
else:
    print("Some error")