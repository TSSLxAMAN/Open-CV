import cv2

img = cv2.imread('images/image.jpg')
resized_img = cv2.resize(img,(700,700))

# gaussian_img = cv2.GaussianBlur(resized_img,(21,21) -> kernal size decides teh capacity of the bluring image 21 is max 3 is min ,100 -> Sigma)
gaussian_img = cv2.GaussianBlur(resized_img,(21,21),100)
if gaussian_img is not None:
    cv2.imshow("Original Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Blurred Iamge", gaussian_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Some error Occured")