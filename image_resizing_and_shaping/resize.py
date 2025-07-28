import cv2

image = cv2.imread('images/image.jpg')

if image is not None:
    resized_img = cv2.resize(image, (300 , 300))

    cv2.imshow("Original ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Resized ", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("output_images/resized_images.jpg",resized_img)
    print("Image saved!!")

else:
    print("Some error")