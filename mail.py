import xlrd
from xlutils.copy import copy
import xlrd
from xlutils.copy import copy

# Open existing database
rb = xlrd.open_workbook("db.xls")

sheet = rb.sheet_by_name("info")

row = sheet.nrows

wb = copy(rb)

ws = wb.get_sheet(0)
folder = "QRDB"

if not os.path.exists(folder):
    os.mkdir(folder)

op = 1

while op == 1:

    print("\n===== Student Registration =====")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile Number: ")

    # Generate ID
    idd = "TN" + name[:2].upper() + mobile[:2] + "20"

    # Save Data
    ws.write(row, 0, row)
    ws.write(row, 1, name)
    ws.write(row, 2, email)
    ws.write(row, 3, mobile)
    ws.write(row, 4, idd)

    print("\nStudent Added Successfully!")
    print("Generated ID:", idd)

    row += 1

    op = int(input("\nAdd another student? (1=Yes, 0=No): "))

wb.save("db.xls")

print("\nDatabase Saved Successfully.")