import gspread
from Private import private_keys

service_account = gspread.service_account(filename="Private/Google_Sheets_API.json")
google_sheets = service_account.open_by_key(private_keys.google_sheets_id)

worksheet = google_sheets.worksheet("discord registrations")

def add_a_person(user):
    worksheet.append_row(user)
