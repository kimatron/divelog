import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import copy
import os
from colorama import init, Fore, Style

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
    print(Fore.BLUE + """
░█▀▀░█▀▀░█░█░█▀▄░█▀█░░░█▀▄░▀█▀░█░█░█▀▀░░░█░░░█▀█░█▀▀
░▀▀█░█░░░█░█░█▀▄░█▀█░░░█░█░░█░░▀▄▀░█▀▀░░░█░░░█░█░█░█
░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀░▀░░░▀▀░░▀▀▀░░▀░░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀
    """)


display_logo()


def add_dive_log():
    # Prompt the user to enter dive log information
    dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")

    # Validate the dive date format
    while True:
        try:
            dive_date = datetime.strptime(dive_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. \
            Please enter the date in YYYY-MM-DD format.")
            dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")

    dive_buddy = input("Enter Dive Buddy Name:\n ")
    dive_site = input("Enter Dive Site Name:\n ")
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
        starting_air = input("Enter Starting Air (in PSI):\n ")
        if not int(starting_air):
            print("Invalid input. Please enter an integer.")
            continue
        elif int(starting_air) < 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        else:
            break

    while True:
        ending_air = input("Enter Ending Air (in PSI):\n ")
        if not int(ending_air):
            print("Invalid input. Please enter an integer.")
            continue
        elif int(ending_air) < 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        elif int(starting_air) < int(ending_air):
            print("Invalid input. Please enter number less than starting air.")
            continue
        else:
            break

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


def delete_dive_log():
    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Get all dive logs from the spreadsheet
    dive_logs = spreadsheet.get_all_records()

    while True:
        # Check if there are dive logs to delete
        if not dive_logs:
            print("No dive logs found to delete.")
            return

        # Display the list of dive logs to the user
        print("------- Dive Logs -------")
        for index, log in enumerate(dive_logs, start=1):
            print(f"{index}."
                  f" Dive Date: {log['Dive Date']}, "
                  f" Dive Buddy: {log['Dive Buddy Name']},"
                  f" Dive Site: {log['Dive Site Name']}")

        # Prompt the user to select a dive log to delete
        dive_index = input("Enter the index of the dive log to delete "
                           " (or 'q' to quit):\n ")

        if dive_index == 'q':
            return

        try:
            # Convert the input to an integer and ensure it's a valid index
            dive_index = int(dive_index)
            if dive_index < 1 or dive_index > len(dive_logs):
                print("Invalid dive log index.")
                continue

            # Prompt the user for confirmation
            confirmation = input("Are you sure you want to "
                                 " delete this dive log? (y/n)\n ")

            if confirmation.lower() != 'y':
                print("Dive log deletion canceled.")
                continue

            # Delete the selected dive log
            # Add 1 to account for the header row
            spreadsheet.delete_rows(dive_index + 1)

            print("Dive log deleted successfully!")

            # Update the dive_logs list after deleting a log
            dive_logs = copy.copy(spreadsheet.get_all_records())

            # Prompt the user to delete another dive log
            delete_another = input("Do you want to delete "
                                   " another dive log? (y/n)\n ")
            if delete_another.lower() != 'y':
                return
        except ValueError:
            print("Invalid input. Please enter a number.")


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
    print(Fore.MAGENTA + "------- Dive Logs -------" + Style.RESET_ALL)
    for index, log in enumerate(dive_logs, start=1):
        print(Fore.YELLOW + f"Dive {index}:" + Style.RESET_ALL)
        print(Fore.GREEN + f"Dive Date: {log['Dive Date']}")
        print(f"Dive Buddy: {log['Dive Buddy Name']}")
        print(f"Dive Site: {log['Dive Site Name']}")
        print(f"Dive Depth: {log['Dive Depth']}")
        print(f"Dive Time: {log['Dive Time']}")
        print(f"Starting Air: {log['Starting Air']}")
        print(f"Ending Air: {log['Ending Air']}")
        print(Fore.MAGENTA + "------------------------" + Style.RESET_ALL)


def search_dive_logs():
    # Get the search query from the user
    search_query = input("Enter a specific search query "
                         "(Dive Site Name, Dive Buddy, Dive Date...):\n ")

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


def display_about():
    print(Style.BRIGHT + Fore.CYAN + """
    === About ===
    This program is a dive log application that
    allows users to record and manage their scuba dive logs.
    It provides features such as adding new dive logs,
    deleting existing dive logs, searching dive logs,
    and viewing all previous dive logs.

    Developed by [Kim Hanlon]
    Version: 1.0
    """ + Style.RESET_ALL)


def display_instructions():
    print(Style.BRIGHT + Fore.BLUE+"""
======= Instructions =======

1. View Dive Logs:
   - This option allows you to view all the existing dive logs
   in numerical order.

2. Add Dive Log:
   - Use this option to add a new dive log to the database.
   - You will be prompted to enter information such as the dive date,
   dive buddy name, and dive site name.
   Dive time is to be entered in minutes and requires an integer input;
   Dive depth is to be entered in meters and requires an integer input;
   Starting and Ending air is to be entered in PSI
   and requires an integer input.


3. Delete Dive Log:
   - Select this option to delete a dive log from the database.
   - You will be prompted to select the dive log to delete from a list.
   - Confirmation is required before log deletion is completed.

4. Search Dive Logs:
   - This option enables you to search dive logs
   based on certain criteria: dive date, dive buddy name, or dive site name.

5. Instructions:
   - This option displays these instructions for using the dive log program.

6. About:
   - This option provides information about the dive log program
   and the developer.

0. Exit:
   - Select this option to exit the dive log program.

===========================
""" + Style.RESET_ALL)


def display_goodbye():
    print(f"{Style.BRIGHT}{Fore.BLUE}See you after the next dive!")
    print(f"""          )    O
               (   o . O
                )   () .
               /  O   o
             _.|._ o .()
  _         / _:_ \\
 <_><)     |.(_"_).|
    __     _\\. : ./_
 |><_'>   / |..:..| \\
         /_/ `---' \\_\\       ,
 ,  (.   \\_)        \\_)  \\)-<
 _) \\)~    \\   T   /    ,(_)
_/ -(-<    _)__|__(_    \\_)-<~
\\)~ )-<  /....|....\\  .~(_,_"
>(_ (_/   """""" """"""    _\\
`-.__)__\\_.----'`-.______.-'  `-.__
                                       kim
""")
    print(Style.RESET_ALL)
    exit()


def clean_up_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    display_logo()
    print(f"{Style.BRIGHT}{Fore.YELLOW}======= Main Menu =======")
    print(f"{Fore.GREEN}1. View Dive Logs")
    print(f"{Fore.GREEN}2. Add Dive Log")
    print(f"{Fore.GREEN}3. Delete Dive Log")
    print(f"{Fore.GREEN}4. Search Dive Logs")
    print(f"{Fore.CYAN}5. Instructions")
    print(f"{Fore.CYAN}6. About")
    print(f"{Fore.RED}0. Exit")
    print(f"{Style.BRIGHT}{Fore.YELLOW}====================={Style.RESET_ALL}")

# Set the flag variable to True to enter the main menu loop


running = True

while running:
    clean_up_terminal()
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
        # Call the display_instructions function
        display_instructions()
    elif option == "6":
        # Call the display_about function
        display_about()
    elif option == "0":
        # Call the display_goodbye function
        display_goodbye()
    else:
        print("Invalid option. Please try again.")

    if running:
        input("Press Enter to go back to the Main Menu.\n")
        clean_up_terminal()

display_logo()

while True:
    display_main_menu()


def main():
    display_logo()
    set_up_menu()
    display_main_menu()


if __name__ == "__main__":
    main()
