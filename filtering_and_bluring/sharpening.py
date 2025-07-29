import cv2
import numpy as np
img = cv2.imread('images/image.jpg')
resized_img = cv2.resize(img,(700,700))
sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpen_img = cv2.filter2D(resized_img,-50,sharpen_kernel)
if sharpen_img is not None:
    cv2.imshow("Original Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Blurred Iamge", sharpen_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Some error Occured")