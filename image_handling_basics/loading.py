import cv2

# img = cv2.imread('images/image.jpg')
img2 = cv2.imread('images/1.png')

# print(img)
# print(img2) this prints the matrix og the image 

if img2 is not None:
    print("Image loaded successfully")
else:
    print("Some error")