import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request

    # Connect to the Google Sheets API and authenticate using the API credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("divelog.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Dive Log")



def add_dive_log():
    # Prompt the user to enter dive log information
    dive_number = input("Enter Dive Number: ")
    dive_buddy = input("Enter Dive Buddy Name: ")
    dive_site = input("Enter Dive Site Name: ")
    dive_depth = input("Enter Dive Depth: ")
    dive_time = input("Enter Dive Time: ")
    starting_air = input("Enter Starting Air: ")
    ending_air = input("Enter Ending Air: ")

    # Validate the input data (you can customize the validation rules as per your requirements)
    if not (dive_number and dive_buddy and dive_site and dive_depth and dive_time and starting_air and ending_air):
        print("Error: All fields are required.")
        return



    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")
    

    # Add the dive log data to the Google Sheets spreadsheet
    new_row = [dive_number, dive_buddy, dive_site, dive_depth, dive_time, starting_air, ending_air]
    spreadsheet.append_row(new_row)

    print("Dive log added successfully!")

""" Call the add_dive_log function
add_dive_log()
"""
def delete_dive_log():
    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Get all dive logs from the spreadsheet
    dive_logs = spreadsheet.get_all_records()

    # Check if there are dive logs to delete
    if not dive_logs:
        print("No dive logs found to delete.")
        return

    # Display the list of dive logs to the user
    print("------- Dive Logs -------")
    for index, log in enumerate(dive_logs, start=1):
        print(f"{index}. Dive Number: {log['Dive Number']}, Dive Buddy: {log['Dive Buddy Name']}, Dive Site: {log['Dive Site Name']}")

    # Prompt the user to select a dive log to delete
    dive_index = input("Enter the index of the dive log to delete: ")

    try:
        # Convert the input to an integer and ensure it's a valid index
        dive_index = int(dive_index)
        if dive_index < 1 or dive_index > len(dive_logs):
            print("Invalid dive log index.")
            return

        # Delete the selected dive log
        spreadsheet.delete_rows(dive_index + 1)  # Add 1 to account for the header row

        print("Dive log deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Call the delete_dive_log function
delete_dive_log()
