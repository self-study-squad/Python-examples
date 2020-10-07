# Test 02

import openpyxl
import openpyexcel
wb = openpyxl.load_workbook("example.xlsx")
print(wb.sheetnames)
wb.get_active_sheet()