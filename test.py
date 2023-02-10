import openpyxl
import threading

def update_excel_file():
    # Load the Excel workbook
    workbook = openpyxl.load_workbook("example.xlsx")
    # Select the active worksheet
    worksheet = workbook.active
    # Update a cell value
    worksheet["A1"] = "Updated Value"
    # Save the workbook
    workbook.save("example.xlsx")

# Create a thread
thread = threading.Thread(target=update_excel_file)
# Start the thread
thread.start()

