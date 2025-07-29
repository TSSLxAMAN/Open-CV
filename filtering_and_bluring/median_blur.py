import cv2

img = cv2.imread('images/image.jpg')
resized_img = cv2.resize(img,(700,700))

# median_img = cv2.GaussianBlur(resized_img,21 -> kernal size decides teh capacity of the bluring image 21 is max 3 is min)
median_img = cv2.medianBlur(resized_img, 5)
if median_img is not None:
    cv2.imshow("Original Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Blurred Iamge", median_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Some error Occured")