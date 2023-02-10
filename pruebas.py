import datetime
import xlsxwriter
import time
import openpyxl


Excel_Date = datetime.datetime.now()
print(Excel_Date)

today = Excel_Date.strftime("%h.%d.%Y")
Hours = Excel_Date.strftime("%H.%M.%S")

workbook = xlsxwriter.Workbook('Data_'+ Hours +"_"+ today +'.xlsx')
bold = workbook.add_format({'bold': True})
x=0
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Time', bold)
worksheet.write('B1', 'Light Intensity', bold)

sheet = workbook.sheet_name
# Get a reference to the sheet you want to rename
sheet = workbook._add_sheet("Day 1")



# save changes to workbook
workbook.close()


def update_excel_file(sheet):
    print(Excel_Date)
    time = datetime.datetime.now()
    time = time.strftime("%H.%M.%S")
    # Load the Excel workbook
    workbook = openpyxl.load_workbook('Data_'+ Hours +"_"+ today +'.xlsx')
    # Select the active worksheet
    worksheet = workbook.active
    # Update a cell value
    worksheet["A" + str(sheet)] = time
    worksheet["B" + str(sheet)] = "Updated Value" + str(sheet)
    
    # Save the workbook
    workbook.save('Data_'+ Hours +"_"+ today +'.xlsx')
    

i=2
while True:
    i=i+1
    time.sleep(1)
    Hours = Excel_Date.strftime("%H.%M.%S")
    worksheet.write('A'+str(i), Hours, bold)
    update_excel_file(i)
    
    print(Hours)











 




    


