import cv2

img = cv2.imread('images/1.png')

if img is not None:
    center = (250,250)
    color = (0,0,255)
    radius = 50
    cv2.circle(img,center,radius,color,2)
    cv2.imshow("Line ", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Some error")