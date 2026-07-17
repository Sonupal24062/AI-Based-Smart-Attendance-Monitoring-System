import tkinter as tk
from tkinter import messagebox
import subprocess


# ---------------------- FUNCTIONS ----------------------

def register_student():
    subprocess.run(["python3.13", "register_student.py"])


def create_dataset():
    subprocess.run(["python3.13", "dataset.py"])


def train_model():
    subprocess.run(["python3.13", "trainer.py"])


def start_recognition():
    subprocess.run(["python3.13", "recognizer.py"])


def view_database():
    subprocess.run(["python3.13", "read_database.py"])


def view_attendance():
    subprocess.run(["python3.13", "read_attendance.py"])


def about():
    messagebox.showinfo(
        "About",
        "Face Recognition Attendance System\n\nDeveloped by Sonu Pal"
    )


# ---------------------- WINDOW ----------------------

root = tk.Tk()

root.title("Face Recognition Attendance System")

root.geometry("700x600")

root.resizable(False, False)

root.configure(bg="#EAF4FC")


# ---------------------- TITLE ----------------------

title = tk.Label(
    root,
    text="FACE RECOGNITION ATTENDANCE SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1565C0",
    fg="white",
    pady=15
)

title.pack(fill="x")


# ---------------------- BUTTONS ----------------------

button_style = {
    "font": ("Arial", 14),
    "width": 28,
    "height": 2,
    "bg": "#1976D2",
    "fg": "white",
    "activebackground": "#0D47A1",
    "activeforeground": "white"
}


tk.Button(
    root,
    text="Register Student",
    command=register_student,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="Create Dataset",
    command=create_dataset,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="Train Model",
    command=train_model,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="Start Attendance",
    command=start_recognition,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="View Student Database",
    command=view_database,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="View Attendance",
    command=view_attendance,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="About",
    command=about,
    **button_style
).pack(pady=10)


tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Arial", 14),
    width=28,
    height=2,
    bg="red",
    fg="white"
).pack(pady=20)


# ---------------------- FOOTER ----------------------

footer = tk.Label(
    root,
    text="Developed by Sonu Pal",
    bg="#1565C0",
    fg="white",
    font=("Arial", 11)
)

footer.pack(side="bottom", fill="x")


root.mainloop()