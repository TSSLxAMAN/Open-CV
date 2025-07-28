import cv2

img = cv2.imread('images/1.png')

if img is not None:
    (w , h) = img.shape[:2]
    # print(h)
    # print(w)
    centre = (w//2 ,h//2)
    # M = cv2.getRotationMatrix2D(centre,degree,scale)
    M = cv2.getRotationMatrix2D(centre,90,1.0)
    rotated = cv2.warpAffine(img, M, (w,h))
    cv2.imshow("Original : ",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("Rotated : ",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("output_images/rotated_image.png",rotated)
    print("Image saved")
else:
    print("Some error")