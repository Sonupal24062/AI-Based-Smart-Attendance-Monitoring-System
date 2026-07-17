import xlrd

# Open attendance file
rb = xlrd.open_workbook("Attendance.xls")

sheet = rb.sheet_by_name("Attendance")


print("Rows:", sheet.nrows)
print("Columns:", sheet.ncols)


for i in range(sheet.nrows):
    print(sheet.row_values(i))