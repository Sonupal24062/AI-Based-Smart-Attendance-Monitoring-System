import cv2
import xlrd

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


def get_student_details(student_id):

    for i in range(1, sheet.nrows):

        row = sheet.row_values(i)

        if row[4] == student_id:
            return row[1], row[2], row[3]

    return "Unknown", "", ""


# Haar Cascade
faceCascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)


cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX


while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    faces = faceCascade.detectMultiScale(
        gray,
        1.2,
        5
    )


    for (x,y,w,h) in faces:

        cv2.rectangle(
            img,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )


        id, confidence = recognizer.predict(
            gray[y:y+h,x:x+w]
        )


        if confidence < 70:

            if id in id_map:

                student_id = id_map[id]

                name,email,mobile = get_student_details(student_id)


                text = "Name: " + name

                cv2.putText(
                    img,
                    text,
                    (x,y-50),
                    font,
                    0.7,
                    (255,255,255),
                    2
                )
                cv2.putText(
                    img,
                    "Email: "+email,
                    (x,y),
                    font,
                    0.5,
                    (255,255,255),
                    2
                )
                cv2.putText(
                    img,
                    "Mobile: "+mobile,
                    (x,y+25),
                    font,
                    0.5,
                    (255,255,255),
                    2
                )
                

                cv2.putText(
                    img,
                    "ID: "+student_id,
                    (x,y-25),
                    font,
                    0.7,
                    (255,255,255),
                    2
                )

        else:

            cv2.putText(
                img,
                "Unknown",
                (x,y-10),
                font,
                0.8,
                (255,255,255),
                2
            )


    cv2.imshow(
        "Face Recognition",
        img
    )


    k=cv2.waitKey(10)&0xff

    if k==27:
        break


cam.release()
cv2.destroyAllWindows()