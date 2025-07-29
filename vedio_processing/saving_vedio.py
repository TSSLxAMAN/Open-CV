import cv2
camera = cv2.VideoCapture(0)
# print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(camera.get(cv2.CAP_PROP_FPS))
# print(camera.get(cv2.CAP_PROP_POS_FRAMES))
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

recoder = cv2.VideoWriter("output_images/saving_vedio.avi",codec,20,(frame_width,frame_height))

while True:
    result , frame = camera.read()

    if not result:
        print('Could read Frame')
        break

    recoder.write(frame)
    cv2.imshow('Vedio Capturing ',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        print('Quiting....')
        break

camera.release()
recoder.release()
cv2.destroyAllWindows()