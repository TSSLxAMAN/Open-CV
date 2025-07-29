import cv2

cap = cv2.VideoCapture(0)
while True:
    result, frame = cap.read()
    # print(result,frame)
    # print(frame.size)
    # print(frame.shape)
    if not result:
        print("could not read frame")
        break
    
    cv2.imshow("Vedio capturing",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting")
        break

cap.release()
cv2.destroyAllWindows()
