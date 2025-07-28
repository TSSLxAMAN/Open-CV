import cv2

img = cv2.imread('images/1.png')

if img is not None:
    pt1 = (50,10)
    pt2 = (150,100)
    color = (255,0,0)
    cv2.line(img,pt1,pt2,color,2)
    cv2.imshow("Line ", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Some error")