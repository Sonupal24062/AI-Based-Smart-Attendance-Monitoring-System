import cv2
import os
import xlrd


# Load database
rb = xlrd.open_workbook("db.xls")
sheet = rb.sheet_by_name("info")


# Load Haar Cascade
face_detector = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)


# Ask Student ID
student_id = input("Enter Student ID: ")


# Check student exists
student_found = False

for i in range(1, sheet.nrows):

    row = sheet.row_values(i)

    if row[4] == student_id:
        student_found = True
        break


if not student_found:

    print("Student ID not found in database!")
    exit()


# Open Camera
cam = cv2.VideoCapture(0)


count = 0


while True:

    ret, img = cam.read()

    if not ret:
        print("Camera not found!")
        break


    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )


    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )


    for (x,y,w,h) in faces:

        count += 1


        face = gray[y:y+h, x:x+w]


        cv2.imwrite(
            f"Dataset/User.{student_id}.{count}.jpg",
            face
        )


        cv2.rectangle(
            img,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )


        cv2.putText(
            img,
            f"Image {count}/100",
            (10,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )


    cv2.imshow(
        "Dataset Creator",
        img
    )


    key=cv2.waitKey(1)


    if key==27 or count>=100:
        break



cam.release()

cv2.destroyAllWindows()


print("\nDataset Created Successfully!")