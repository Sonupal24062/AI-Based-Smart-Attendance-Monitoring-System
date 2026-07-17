import cv2
import os
import numpy as np
from PIL import Image

# Create LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Dataset folder
dataset_path = "Dataset"


def get_images_and_labels(path):

    image_paths = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.endswith(".jpg")
    ]

    face_samples = []
    ids = []
    id_mapping = {}

    for image_path in image_paths:

        pil_image = Image.open(image_path).convert("L")

        img_numpy = np.array(pil_image, "uint8")

        filename = os.path.split(image_path)[-1]

        student_id = filename.split(".")[1]

        numeric_id = abs(hash(student_id)) % 100000

        face_samples.append(img_numpy)
        ids.append(numeric_id)

        id_mapping[numeric_id] = student_id
        #save unique ID mapping 
        with open("Trainr/id_mapping.txt", "w") as f:
            for key, value in id_mapping.items():
                f.write(f"{key}:{value}\n")

                return face_samples, ids
                
             

        # Example:
        # User.TNSO9720.1.jpg

        student_id = filename.split(".")[1]

        # Convert ID into number
        numeric_id = abs(hash(student_id)) % 100000

        face_samples.append(img_numpy)
        ids.append(numeric_id)
        mapping_file = "Trainr/id_mapping.txt"

        with open(mapping_file, "a") as f:
            f.write(f"{numeric_id}:{student_id}\n")
        #save ID mapping
        if not os.path.exists("Trainr"):
          os.mkdir("Trainr")
        with open("Trainr/id_mapping.txt", "a") as f:
            f.write(f"{numeric_id}:{student_id}\n")


    return face_samples, ids


print("Training is starting...")

faces, ids = get_images_and_labels(dataset_path)

recognizer.train(faces, np.array(ids))


# Create Trainr folder
if not os.path.exists("Trainr"):
    os.mkdir("Trainr")


# Save trained model
recognizer.write("Trainr/trainer.yml")

print("Training Completed Successfully!")