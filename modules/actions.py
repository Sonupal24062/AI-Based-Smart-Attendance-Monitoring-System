import subprocess
from tkinter import messagebox


def register_student():
    subprocess.Popen(["python3.13", "register_student.py"])


def create_dataset():
    subprocess.run(["python3.13", "dataset.py"])


def train_model():
    subprocess.run(["python3.13", "trainer.py"])


def start_attendance():
    subprocess.run(["python3.13", "recognizer.py"])


def view_students():
    subprocess.Popen(["python3.13", "read_database.py"])


def view_attendance():
    subprocess.run(["python3.13", "read_attendance.py"])


def about():
    messagebox.showinfo(
        "About",
        "Face Recognition Attendance System\n\nDeveloped by Sonu Pal"
    )