import cv2

img = cv2.imread('images/1.png')

if img is not None:
    cv2.putText(img,"This is One",(300,100),2,1.5,(255,0,0),1)
    cv2.imshow("This is text on image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Some error")