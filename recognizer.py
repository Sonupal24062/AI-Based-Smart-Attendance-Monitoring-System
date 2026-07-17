import cv2
import xlrd
from xlutils.copy import copy
from datetime import datetime


# Load recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainr/trainer.yml")


# Load ID mapping
id_map = {}

with open("Trainr/id_mapping.txt", "r") as f:
    for line in f:
        data = line.strip().split(":")
        id_map[int(data[0])] = data[1]


# Load database
rb = xlrd.open_workbook("db.xls")
sheet = rb.sheet_by_name("info")


# Get student details from database
def get_student_details(student_id):

    for i in range(1, sheet.nrows):

        row = sheet.row_values(i)

        if row[4] == student_id:
            return row[1], row[2], row[3]

    return "Unknown", "", ""


# Mark Attendance
def mark_attendance(student_id, name):

    file = "Attendance.xls"

    rb = xlrd.open_workbook(file)

    sheet_att = rb.sheet_by_name("Attendance")


    # Avoid duplicate attendance
    for i in range(1, sheet_att.nrows):

        if sheet_att.cell_value(i, 0) == student_id:
            return


    wb = copy(rb)

    ws = wb.get_sheet(0)

    row = sheet_att.nrows


    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")


    ws.write(row, 0, student_id)
    ws.write(row, 1, name)
    ws.write(row, 2, date)
    ws.write(row, 3, time)


    wb.save(file)

    print("Attendance Marked Successfully")


# Haar Cascade
faceCascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)


# Camera
cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX


while True:

    ret, img = cam.read()

    if not ret:
        print("Camera not found!")
        break


    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )


    faces = faceCascade.detectMultiScale(
        gray,
        1.2,
        5
    )


    for (x, y, w, h) in faces:


        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (255,0,0),
            2
        )


        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )


        if confidence < 70:


            if id in id_map:

                student_id = id_map[id]


                name, email, mobile = get_student_details(student_id)


                # Attendance save
                mark_attendance(student_id, name)


                cv2.putText(
                    img,
                    "Name: " + name,
                    (x, y-60),
                    font,
                    0.7,
                    (255,255,255),
                    2
                )


                cv2.putText(
                    img,
                    "ID: " + student_id,
                    (x, y-35),
                    font,
                    0.7,
                    (255,255,255),
                    2
                )


                cv2.putText(
                    img,
                    "Email: " + email,
                    (x, y-10),
                    font,
                    0.5,
                    (255,255,255),
                    2
                )


                cv2.putText(
                    img,
                    "Mobile: " + mobile,
                    (x, y+15),
                    font,
                    0.5,
                    (255,255,255),
                    2
                )


        else:

            cv2.putText(
                img,
                "Unknown",
                (x, y-10),
                font,
                0.8,
                (255,255,255),
                2
            )


    cv2.imshow(
        "Face Recognition",
        img
    )


    k = cv2.waitKey(10) & 0xff


    if k == 27:
        break



cam.release()

cv2.destroyAllWindows()