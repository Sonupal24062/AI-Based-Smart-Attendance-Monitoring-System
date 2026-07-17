import tkinter as tk
from tkinter import messagebox
import xlrd
from xlutils.copy import copy
import os
import pyqrcode

class RegisterStudent:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Register Student")

        self.root.geometry("500x400")

        tk.Label(
            self.root,
            text="Student Registration",
            font=("Arial",20,"bold")
        ).pack(pady=20)

        tk.Label(self.root,text="Name").pack()

        self.name = tk.Entry(self.root,width=40)
        self.name.pack()

        tk.Label(self.root,text="Email").pack()

        self.email = tk.Entry(self.root,width=40)
        self.email.pack()

        tk.Label(self.root,text="Mobile").pack()

        self.mobile = tk.Entry(self.root,width=40)
        self.mobile.pack()

        tk.Button(
            self.root,
            text="Register",
            command=self.save
        ).pack(pady=20)

        self.root.mainloop()
    def save(self):
        name = self.name.get().strip()
        email = self.email.get().strip()
        mobile = self.mobile.get().strip()

        if name == "" or email == "" or mobile == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return


        database = "db.xls"

        rb = xlrd.open_workbook(database)

        sheet = rb.sheet_by_name("info")

        row = sheet.nrows


        wb = copy(rb)

        ws = wb.get_sheet(0)


        student_id = "TN" + name[:2].upper() + mobile[-2:] + "20"


        ws.write(row,0,row)
        ws.write(row,1,name)
        ws.write(row,2,email)
        ws.write(row,3,mobile)
        ws.write(row,4,student_id)


        wb.save(database)
                # Create QR Folder

        folder = "QRDB"

        if not os.path.exists(folder):
            os.mkdir(folder)


        qr_data = f"""
Name: {name}
Email: {email}
Mobile: {mobile}
ID: {student_id}
"""


        qr = pyqrcode.create(qr_data)


        qr.png(
            f"{folder}/{student_id}.png",
            scale=6
        )


        messagebox.showinfo(
            "Success",
            f"Student Added Successfully\n\nID: {student_id}"
        )


        self.name.delete(0,tk.END)
        self.email.delete(0,tk.END)
        self.mobile.delete(0,tk.END)
if __name__ == "__main__":
    RegisterStudent()
        