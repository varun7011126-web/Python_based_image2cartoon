import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("can't open web came")
    exit()


print("c to capture the image and q to quit the camera")

while True:
    ret,frame=cap.read()

    if not ret:
        print("can't capture the frame")
        break

    cv2.imshow("web-came",frame)

    key=cv2.waitKey(1) & 0xFF

    if key==ord('c'):
        cv2.imwrite("captured-image.jpg",frame)
        print("image saved successfully")

    elif key==ord('q'):
        
        break

cap.release()
cv2.destroyAllWindows()




