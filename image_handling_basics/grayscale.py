import cv2

img = cv2.imread('images/image.jpg')

if img is not None:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscal image',img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('output_images/grayscale.png',img_gray)
else:
    print("Some error")