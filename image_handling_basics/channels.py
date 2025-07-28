import cv2

img = cv2.imread('images/1.png')

# print(img.shape) returns height, width, channels
# print(img.size) it return multiplication of all  height * width * channels

if img is not None:
    width , height , channels = img.shape
    size = img.size
    print(f'width : {width} \nheight : {height} \nchannels : {channels} \nsize : {size}')
else:
    print("Some error")