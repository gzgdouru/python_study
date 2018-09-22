#写xlxs文件
import openpyxl
import json
import os

if __name__ == "__main__":
    data = json.load(open("numbers.txt", "r", encoding="utf8"))

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "numbers"
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.cell(row=i+1, column=j+1, value=str(data[i][j]))
    wb.save("numbers.xlsx")
    wb.close()