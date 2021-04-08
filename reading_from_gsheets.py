import gspread
from Private import private_keys

service_account = gspread.service_account(filename="Private/Google_Sheets_API.json")
google_sheets = service_account.open_by_key(private_keys.google_sheets_id)

worksheet = google_sheets.worksheet("discord registrations")

def get_a_cell(cell):
    return worksheet.get(cell)

def is_available(email):
    user = []
    try:
        data = worksheet.find("hardik.kumar18feb@gmail.com")
        user.append(True)
        user.append(data.row)
        user.append(data.col)
    except gspread.exceptions.CellNotFound:
        user.append(False)

    return user

def get_user_data(row):
    user_data = worksheet.row_values(row)
    return user_data
