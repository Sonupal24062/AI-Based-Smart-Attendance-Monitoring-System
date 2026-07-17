import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera not found!")
        break

    cv2.imshow("My Camera", frame)

    key = cv2.waitKey(1)

    if key == 27:      # ESC key
        break

camera.release()
cv2.destroyAllWindows()