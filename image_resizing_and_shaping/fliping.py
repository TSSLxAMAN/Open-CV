import cv2

img = cv2.imread('images/1.png')

if img is not None:
    # flipped = cv2.flip(img,flipCode) 1 -> horizontal 0-> vertical -1 -> both horizontal and vertical 
    flipped = cv2.flip(img,1)
    cv2.imshow("Original : ",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Rotated : ",flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("output_images/fliped_image.png",flipped)
    print("Image saved")
else:
    print("Some error")