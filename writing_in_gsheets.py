import gspread

service_account = gspread.service_account(filename="Google_Sheets_API.json")
# google_sheets = service_account.open_by_url("https://docs.google.com/spreadsheets/d/173NGS50JENbm55SJ5zCgCRWorvCuTs9GtOEJl6-O1JM/edit#gid=0")
google_sheets = service_account.open_by_key("173NGS50JENbm55SJ5zCgCRWorvCuTs9GtOEJl6-O1JM")

worksheet = google_sheets.worksheet("Sheet1")

user = ['Priyansh', 20, 'Chindwara']

# worksheet.insert_row(user, index=5) #* Insert user in row 3
# worksheet.append_row(user) #* Add a new user below

# worksheet.update_acell("B3", 20) #* Update a particular cell's data
# worksheet.delete_rows(3) #* Deletes a specific row
