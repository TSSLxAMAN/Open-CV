import cv2

img = cv2.imread('images/1.png')

if img is not None:
    cv2.imwrite('output_images/output.png', img)
else:
    print("Some error")