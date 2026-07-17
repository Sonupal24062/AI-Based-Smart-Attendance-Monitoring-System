import xlwt

# Create a new workbook
wb = xlwt.Workbook()

# Create a sheet
sheet = wb.add_sheet("info")

# Write column headings
sheet.write(0, 0, "SN")
sheet.write(0, 1, "Name")
sheet.write(0, 2, "Email")
sheet.write(0, 3, "Mobile No")
sheet.write(0, 4, "ID")

# Save the workbook
wb.save("db.xls")

print("Database created successfully!")