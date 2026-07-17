import xlrd

# Open the workbook
rb = xlrd.open_workbook("db.xls")

# Open the sheet
sheet = rb.sheet_by_name("info")

print("Number of Rows:", sheet.nrows)
print("Number of Columns:", sheet.ncols)

# Print all rows
for i in range(sheet.nrows):
    print(sheet.row_values(i))