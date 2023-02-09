import datetime
from openpyxl import Workbook as Data_File
from openpyxl import load_workbook


wb = Data_File()
now = datetime.datetime.now()
date_time = now.strftime("%d.%m.%Y")

try:
    wb = load_workbook(filename = 'Data_File.xlsx')
    wb.save("Data_File_II.xlsx")
    wb = load_workbook(filename = 'Data_File_II.xlsx')

except:
    wb.save("Data_File.xlsx")
    wb = load_workbook(filename = 'Data_File.xlsx')

#Select the current active sheet








 




    


