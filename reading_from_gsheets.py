import gspread

service_account = gspread.service_account(filename="Google_Sheets_API.json")
# google_sheets = service_account.open_by_url("https://docs.google.com/spreadsheets/d/173NGS50JENbm55SJ5zCgCRWorvCuTs9GtOEJl6-O1JM/edit#gid=0")
google_sheets = service_account.open_by_key("173NGS50JENbm55SJ5zCgCRWorvCuTs9GtOEJl6-O1JM")

worksheet = google_sheets.worksheet("Sheet1")
data1 = worksheet.get_all_records()
data2 = worksheet.get_all_values()
data3 = worksheet.row_values(2)
data4 = worksheet.get("A2")

# print(data1, "\n") #* Data comes in as list of dictonaries
# print(data2, "\n") #* Data comes in as list of lists(one row each)
# print(data3, "\n") #* Gets only one row data in the form of list
print(data4, "\n") #* Single data in list of list
