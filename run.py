import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Connect to the Google Sheets API and authenticate using the API credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Dive Log")


def display_logo():
    print("""
░█▀▀░█▀▀░█░█░█▀▄░█▀█░░░█▀▄░▀█▀░█░█░█▀▀░░░█░░░█▀█░█▀▀
░▀▀█░█░░░█░█░█▀▄░█▀█░░░█░█░░█░░▀▄▀░█▀▀░░░█░░░█░█░█░█
░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀░▀░░░▀▀░░▀▀▀░░▀░░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀
    """)


display_logo()


def add_dive_log():
    # Prompt the user to enter dive log information
    dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")
    dive_buddy = input("Enter Dive Buddy Name:\n ")
    dive_site = input("Enter Dive Site Name:\n ")

    # Validate the dive date format
    while True:
        try:
            dive_date = datetime.strptime(dive_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. \
            Please enter the date in YYYY-MM-DD format.")
            dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")

    # Validate input for numeric fields
    while True:
        try:
            dive_depth = int(input("Enter Dive Depth (in meters):\n "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    while True:
        try:
            dive_time = int(input("Enter Dive Time (in minutes):\n "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    while True:
        try:
            starting_air = int(input("Enter Starting Air (in PSI):\n "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    while True:
        try:
            ending_air = int(input("Enter Ending Air (in PSI):\n "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Validate the input data
    if not (dive_date and dive_buddy and dive_site):
        print("Error: All fields are required.")
        return

    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Add the dive log data to the Google Sheets spreadsheet
    new_row = [str(dive_date),
               dive_buddy,
               dive_site,
               dive_depth,
               dive_time,
               starting_air,
               ending_air]
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
        print(f"{index}. Dive Date: {log['Dive Date']}, Dive Buddy: {log['Dive Buddy Name']}, Dive Site: {log['Dive Site Name']}")

    # Prompt the user to select a dive log to delete
    dive_index = input("Enter the index of the dive log to delete:\n ")

    try:
        # Convert the input to an integer and ensure it's a valid index
        dive_index = int(dive_index)
        if dive_index < 1 or dive_index > len(dive_logs):
            print("Invalid dive log index.")
            return

        # Delete the selected dive log
        # Add 1 to account for the header row
        spreadsheet.delete_rows(dive_index + 1)

        print("Dive log deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")


""" Call the delete_dive_log function
delete_dive_log()
"""


def view_dive_logs():
    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Get all dive logs from the spreadsheet
    dive_logs = spreadsheet.get_all_records()

    # Check if there are dive logs to view
    if not dive_logs:
        print("No dive logs found.")
        return

    # Display the dive logs to the user
    print("------- Dive Logs -------")
    for index, log in enumerate(dive_logs, start=1):
        print(f"Dive {index}:")
        print(f"Dive Date: {log['Dive Date']}")
        print(f"Dive Buddy: {log['Dive Buddy Name']}")
        print(f"Dive Site: {log['Dive Site Name']}")
        print(f"Dive Depth: {log['Dive Depth']}")
        print(f"Dive Time: {log['Dive Time']}")
        print(f"Starting Air: {log['Starting Air']}")
        print(f"Ending Air: {log['Ending Air']}")
        print("------------------------")


""" Call the view_dive_logs function
view_dive_logs()
"""


def search_dive_logs():
    # Get the search query from the user
    search_query = input("Enter a specific search query \
    (Dive Site Name, Dive Buddy, Dive Date...):\n ")

    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Create a list to store the matching dive logs
    matching_logs = []

    # Get all dive logs from the spreadsheet
    dive_logs = spreadsheet.get_all_records()

    # Iterate over each dive log
    for log in dive_logs:
        # Check if any field in the log contains the search query
        if search_query.lower() in [str(value).lower()
                                    for value in log.values()]:
            # Add the matching log to the list
            matching_logs.append(log)

    # Check if there are matching dive logs
    if not matching_logs:
        print("No matching dive logs found.")
        return

    # Display the matching dive logs to the user
    print("------- Matching Dive Logs -------")
    for index, log in enumerate(matching_logs, start=1):
        print(f"Dive {index}:")
        print(f"Dive Date: {log['Dive Date']}")
        print(f"Dive Buddy: {log['Dive Buddy Name']}")
        print(f"Dive Site: {log['Dive Site Name']}")
        print(f"Dive Depth: {log['Dive Depth']}")
        print(f"Dive Time: {log['Dive Time']}")
        print(f"Starting Air: {log['Starting Air']}")
        print(f"Ending Air: {log['Ending Air']}")
        print("------------------------")


""" Call the search_dive_logs function
search_dive_logs()
"""


def display_main_menu():
    print("======= Main Menu =======")
    print("1. View Dive Logs")
    print("2. Add Dive Log")
    print("3. Delete Dive Log")
    print("4. Search Dive Logs")
    print("5. Export Dive Logs")
    print("0. Exit")
    print("========================")

# Set the flag variable to True to enter the main menu loop


running = True

while running:
    display_main_menu()

    option = input("Enter an option:\n ")

    if option == "1":
        # Call the view_dive_logs function
        view_dive_logs()
    elif option == "2":
        # Call the add_dive_log function
        add_dive_log()
    elif option == "3":
        # Call the delete_dive_log function
        delete_dive_log()
    elif option == "4":
        # Call the search_dive_logs function
        search_dive_logs()
    elif option == "5":
        # Call the export_dive_logs function
        export_dive_logs()
    elif option == "0":
        print("See you after the next dive!")
        exit()
    else:
        print("Invalid option. Please try again.")

    if running:
        input("Press Enter to go back to the Main Menu.\n")

display_logo()

while True:
    display_main_menu()
