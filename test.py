from openpyxl import load_workbook
wb = load_workbook("demo.xlsx") 
# Sheet is the SheetName where the data has to be entered
sheet = wb["Sheet"]
# Enter into 1st row and Ath column
sheet['A1'] = 'Software Testing Help'
# Similarly you can enter in the below shown fashion
sheet.cell(row=2, column=1).value = 'OpenPyxl Tutorial'
sheet['B1'] = 10   
sheet.cell(row=2, column=2).value =13.4
wb.save("demo.xlsx")