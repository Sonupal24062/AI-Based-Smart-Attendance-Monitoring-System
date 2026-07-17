#part1
from modules.actions import *

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pandas as pd
import os


class Dashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1400x800")
        self.root.configure(bg="#F4F6F9")
        self.root.resizable(False, False)

        # ================= HEADER =================

        header = tk.Frame(
            self.root,
            bg="#0B5ED7",
            height=80
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Arial", 24, "bold"),
            bg="#0B5ED7",
            fg="white"
        ).pack(pady=18)

        # ================= LEFT MENU =================

        self.menu = tk.Frame(
            self.root,
            bg="#1E293B",
            width=250
        )

        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        tk.Label(
            self.menu,
            text="MENU",
            font=("Arial", 18, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(pady=20)

        buttons = [

            ("Register Student", register_student),

            ("Student Database", view_students),

            ("Create Dataset", create_dataset),

            ("Train Model", train_model),

            ("Start Attendance", start_attendance),

            ("View Attendance", view_attendance),

            ("About", about),

            ("Exit", self.root.destroy)

        ]

        for text, command in buttons:

            tk.Button(

                self.menu,

                text=text,

                width=24,

                height=2,

                command=command,

                bg="#2563EB",

                fg="white",

                font=("Arial", 11, "bold"),

                relief="flat"

            ).pack(pady=6)
                    # ================= RIGHT CONTENT =================

        self.content = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        self.content.pack(
            side="left",
            expand=True,
            fill="both"
        )

        # ================= DASHBOARD CARDS =================

        card_frame = tk.Frame(
            self.content,
            bg="#F4F6F9"
        )

        card_frame.pack(pady=30)

        self.student_card = self.create_card(
            card_frame,
            "Total Students",
            "0",
            0,
            0
        )

        self.attendance_card = self.create_card(
            card_frame,
            "Today's Attendance",
            "0",
            0,
            1
        )

        self.dataset_card = self.create_card(
            card_frame,
            "Dataset Images",
            "0",
            1,
            0
        )

        self.model_card = self.create_card(
            card_frame,
            "Model Status",
            "Not Trained",
            1,
            1
        )

        # ================= WELCOME =================

        tk.Label(
            self.content,
            text="Welcome, Sonu Pal",
            font=("Arial", 26, "bold"),
            bg="#F4F6F9"
        ).pack(pady=20)

        self.time_label = tk.Label(
            self.content,
            font=("Arial", 18),
            bg="#F4F6F9"
        )

        self.time_label.pack()

        self.update_clock()

        self.refresh_dashboard()

        # ================= FOOTER =================

        tk.Label(
            self.root,
            text="Developed by Sonu Pal",
            bg="#0B5ED7",
            fg="white",
            font=("Arial", 12)
        ).pack(side="bottom", fill="x")

        self.root.mainloop()

      # ================= CREATE CARD =================
#part3
    def create_card(self, parent, title, value, row, column):

        frame = tk.Frame(
            parent,
            bg="white",
            width=260,
            height=120,
            bd=1,
            relief="solid"
        )

        frame.grid(
            row=row,
            column=column,
            padx=20,
            pady=15
        )

        frame.grid_propagate(False)

        tk.Label(
            frame,
            text=title,
            font=("Arial", 14, "bold"),
            bg="white"
        ).pack(pady=(15, 5))

        value_label = tk.Label(
            frame,
            text=value,
            font=("Arial", 24, "bold"),
            fg="#0B5ED7",
            bg="white"
        )

        value_label.pack()

        return value_label

    # ================= CLOCK =================

    def update_clock(self):

        now = datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p")

        self.time_label.config(text=now)

        self.root.after(1000, self.update_clock)
            # ================= REFRESH DASHBOARD =================

    def refresh_dashboard(self):

        # Total Students
        try:
            df = pd.read_excel("db.xls")
            self.student_card.config(text=str(len(df)))
        except:
            self.student_card.config(text="0")

        # Attendance
        try:
            df = pd.read_excel("Attendance.xls")
            self.attendance_card.config(text=str(len(df)))
        except:
            self.attendance_card.config(text="0")

        # Dataset Images
        try:
            total_images = 0

            if os.path.exists("Dataset"):

                for file in os.listdir("Dataset"):

                    if file.lower().endswith((".jpg", ".jpeg", ".png")):
                        total_images += 1

            self.dataset_card.config(text=str(total_images))

        except:
            self.dataset_card.config(text="0")

        # Model Status

        if os.path.exists("Trainr/trainer.yml"):

            self.model_card.config(
                text="Trained",
                fg="green"
            )

        else:

            self.model_card.config(
                text="Not Trained",
                fg="red"
            )

        self.root.after(
            5000,
            self.refresh_dashboard
        )


if __name__ == "__main__":
    Dashboard()      