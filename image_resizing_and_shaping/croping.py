import cv2

img = cv2.imread('images/image.jpg')
# print(img.shape) -> (4624, 3472, 3)
if img is not None:
    # cropped_image = img[y_start : y_end , x_start : x_end]
    cropped_image = img[1000:2000 , 1000:2000]
    # print(cropped_image)
    cv2.imshow("Cropped image",cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('output_images/cropped_images.jpg',cropped_image)
    print("Image saved successfully !!")
else:
    print("Some error")