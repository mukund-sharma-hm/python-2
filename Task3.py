import openpyxl
from Task1 import day_details

def write_to_excel(day_details):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name of the Day", "Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
    for day, details in day_details.items():
        ws.append([day, *details])
    wb.save("my_workbook.xlsx")

write_to_excel(day_details)
