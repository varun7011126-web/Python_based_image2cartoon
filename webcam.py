import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("can't open the webcam")
    exit()


print("enter q to close the camera")


while True:
    ret, frame=cap.read()

    if not ret:
        print("can't capture frame")
        break

    cv2.imshow("webcame",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

