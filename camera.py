import cv2

# Load Haar Cascade XML file
face_cascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

# Open webcam
camera = cv2.VideoCapture(0)

while True:

    # Read one frame
    ret, frame = camera.read()

    if not ret:
        print("Camera not found!")
        break

    # Convert image to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Show camera window
    cv2.imshow("Face Detection", frame)

    # Press ESC to close
    if cv2.waitKey(1) == 27:
        break

# Release camera
camera.release()

# Close all windows
cv2.destroyAllWindows()