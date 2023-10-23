from openpyxl import load_workbook
import mysql.connector

#Excel
workbook = load_workbook('Nissan_Order.xlsx')
sheet = workbook.active

values = []
for row in sheet.iter_row(min_row=10, values_only=True):
    print(row)
    values.append(row)


