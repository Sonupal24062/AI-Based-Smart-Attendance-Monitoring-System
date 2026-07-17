import xlwt
import os
from datetime import datetime


file_name = "Attendance.xls"


def create_attendance():

    if not os.path.exists(file_name):

        wb = xlwt.Workbook()

        sheet = wb.add_sheet("Attendance")

        sheet.write(0,0,"ID")
        sheet.write(0,1,"Name")
        sheet.write(0,2,"Date")
        sheet.write(0,3,"Time")

        wb.save(file_name)

        print("Attendance File Created")


create_attendance()