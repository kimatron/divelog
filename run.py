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
    """
    Function to display Scuba Dive Log Logo
    """
    print(Fore.BLUE + """
░█▀▀░█▀▀░█░█░█▀▄░█▀█░░░█▀▄░▀█▀░█░█░█▀▀░░░█░░░█▀█░█▀▀
░▀▀█░█░░░█░█░█▀▄░█▀█░░░█░█░░█░░▀▄▀░█▀▀░░░█░░░█░█░█░█
░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀░▀░░░▀▀░░▀▀▀░░▀░░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀
    """)


display_logo()


def add_dive_log():
    """
    Function to prompt the user to enter
    dive log information and add it to the dive log database
    """
    # Prompt the user to enter dive log information
    dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")

    # Validate the dive date format
    while True:
        if not dive_date:
            print("Error: Date of Dive is required.")
            dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")
        else:
            try:
                dive_date = datetime.strptime(dive_date, "%Y-%m-%d").date()
                if dive_date > datetime.now().date():
                    print(Fore.RED + "Date of Dive "
                          "cannot be in the future." + Style.RESET_ALL)
                    dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Invalid date format. "
                      "Please enter the date "
                      "in YYYY-MM-DD format." + Style.RESET_ALL)
                dive_date = input("Enter Date of Dive (YYYY-MM-DD):\n ")

    dive_buddy = input("Enter Dive Buddy Name:\n ")
    while not dive_buddy or dive_buddy.isdigit():
        print(Fore.RED + "Error: "
              "Dive Buddy Name is required." + Style.RESET_ALL)
        dive_buddy = input("Enter Dive Buddy Name:\n ")

    dive_site = input("Enter Dive Site Name:\n ")
    while not dive_site or dive_site.isdigit():
        print(Fore.RED + "Error: Dive Site Name is required."
              + Style.RESET_ALL)
        dive_site = input("Enter Dive Site Name:\n ")

    # Validate input for numeric fields
    dive_depth = None
    while dive_depth is None:
        dive_depth_input = input("Enter Dive Depth (in meters):\n")
        if not dive_depth_input or \
                not dive_depth_input.isdigit() or \
                int(dive_depth_input) <= 0:
            print(
                Fore.RED + "Error: Dive Depth is required "
                "and must be a positive integer." + Style.RESET_ALL)
            continue

        try:
            dive_depth = int(dive_depth_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    dive_time = None
    while dive_time is None:
        dive_time_input = input("Enter Dive Time (in minutes):\n ")
        if not dive_time_input or \
                not dive_time_input.isdigit() or \
                int(dive_depth_input) <= 0:
            print(
                Fore.RED + "Error: Dive Time is required and must "
                "be a positive integer." + Style.RESET_ALL)
            continue

        try:
            dive_time = int(dive_time_input)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer."
                  + Style.RESET_ALL)

    starting_air = None
    while starting_air is None:
        starting_air_input = input("Enter Starting Air (in PSI):\n ")
        if not starting_air_input:
            print(Fore.RED + "Error: Starting Air is required."
                  + Style.RESET_ALL)
            continue

        if not starting_air_input.isnumeric():
            print(Fore.RED + "Invalid input. Please enter an integer."
                  + Style.RESET_ALL)
            continue

        starting_air = int(starting_air_input)

    ending_air = None
    while ending_air is None:
        ending_air_input = input("Enter Ending Air (in PSI):\n ")
        if not ending_air_input:
            print(Fore.RED + "Error: Ending Air is required."
                  + Style.RESET_ALL)
            continue

        if not ending_air_input.isnumeric():
            print(Fore.RED + "Invalid input. Please enter an integer."
                  + Style.RESET_ALL)
            continue

        if int(starting_air_input) < int(ending_air_input):
            print(
                Fore.RED + "Invalid input. Please enter a number "
                "less than starting air." + Style.RESET_ALL)
            continue

        ending_air = int(ending_air_input)

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

    print(Fore.GREEN + "Dive log added successfully!" + Style.RESET_ALL)

    # Prompt the user to add another dive or return to the main menu
    while True:
        add_another = input("Add another dive? (y/n):\n ")
        if add_another.lower() == "y":
            # Call the add_dive_log() function again to add another dive log
            add_dive_log()
            break
        elif add_another.lower() == "n":
            return
        else:
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'."
                  + Style.RESET_ALL)


def delete_dive_log():
    # Function to delete a dive log from the Google Sheets spreadsheet

    # Open the dive log database (Google Sheets spreadsheet)
    spreadsheet = SHEET.worksheet("DiveLog")

    # Get all dive logs from the spreadsheet
    dive_logs = spreadsheet.get_all_records()

    # Check if there are dive logs to delete
    if not dive_logs:
        print(Fore.YELLOW + "No dive logs found to delete." + Style.RESET_ALL)
        return

    while True:
        # Display the list of dive logs to the user
        print(Fore.MAGENTA + "------- Dive Logs -------" + Style.RESET_ALL)
        for index, log in enumerate(dive_logs, start=1):
            print(f"{index}. Dive Date: {log['Dive Date']},"
                  f" Dive Buddy: {log['Dive Buddy Name']},"
                  f" Dive Site: {log['Dive Site Name']}")

        # Prompt the user to select a dive log to delete
        dive_index = input(
            "Enter the index of the dive log to delete "
            "(or 'm' to go back to the main menu):\n")

        if dive_index.lower() == 'm':
            return  # Go back to the main menu

        try:
            # Convert the input to an integer and ensure it's a valid index
            dive_index = int(dive_index)
            if dive_index < 1 or dive_index > len(dive_logs):
                raise ValueError

            # Prompt the user for confirmation
            confirmation = input(Fore.YELLOW +
                                 "Are you sure you want to delete this"
                                 " dive log? (y/n)\n" + Style.RESET_ALL)

            if confirmation.lower() != 'y':
                print("Dive log deletion canceled.")
            else:
                # Add 1 to account for the header row
                spreadsheet.delete_rows(dive_index + 1)
                print(Fore.GREEN + "Dive log deleted successfully!"
                      + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid index."
                  + Style.RESET_ALL)

        # Prompt the user to delete another dive log
        while True:
            delete_another = input(
                "Do you want to delete another dive log? (y/n)\n")
            if delete_another.lower() == 'n':
                return  # Return from the function to go back to the main menu
            elif delete_another.lower() == 'y':
                break
            else:
                print(Fore.RED + "Invalid input. Please enter 'y' or 'n'."
                      + Style.RESET_ALL)


def view_dive_logs():
    """
    Function to view all dive logs from the Google Sheets spreadsheet
    """

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

        # Print "Please scroll to see all logs" message at the end
        if index == len(dive_logs):
            print(Fore.CYAN + "Please scroll "
                  "to see all logs" + Style.RESET_ALL)


def search_dive_logs():
    """
    Function to search dive logs based on user input query
    """
    while True:
        # Get the search query from the user
        search_query = input(
            "Enter a specific search query "
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
            if search_query.lower() in [
                str(value).lower() for value in log.values()
            ]:
                # Add the matching log to the list
                matching_logs.append(log)

        # Check if there are matching dive logs
        if not matching_logs:
            print(Fore.GREEN + "No matching dive logs found."
                  + Style.RESET_ALL)
            search_again = input(
                "Would you like to search for another dive log? (Y/N):\n ")
            while search_again.lower() != "y" and search_again.lower() != "n":
                print(Style.BRIGHT + Fore.RED + "Invalid input. "
                      "Please enter 'Y' or 'N'." + Style.RESET_ALL)
                search_again = input(
                    "Would you like to search for another dive log? (Y/N):\n ")
            if search_again.lower() == "n":
                return
            else:
                continue

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

            # Print "Please scroll to see all logs" message at the end
            if index == len(matching_logs):
                print(Fore.CYAN + "Please scroll "
                      "to see all logs" + Style.RESET_ALL)

        search_again = input(
            "Would you like to search for another dive log? (Y/N):\n ")
        while search_again.lower() != "y" and search_again.lower() != "n":
            print(Style.BRIGHT + Fore.RED + "Invalid input. "
                  "Please enter 'Y' or 'N'." + Style.RESET_ALL)
            search_again = input(
                "Would you like to search for another dive log? (Y/N):\n ")
        if search_again.lower() == "n":
            return


def display_about():
    """
    Function to display information about the dive log program and developer
    """
    print(Style.BRIGHT + Fore.CYAN + """
    === About ===
    This program is a dive log application that
    allows users to record and manage their scuba dive logs.
    It provides features such as adding new dive logs,
    deleting existing dive logs, searching dive logs,
    and viewing all previous dive logs.

    Developed by [Kim Hanlon]
    GitHub [github.com/kimatron]
    Version: 1.0
    """ + Style.RESET_ALL)


def display_instructions():
    """
    Function to display instructions for using the dive log program
    """
    print(Style.BRIGHT + Fore.BLUE+"""
======= Instructions =======

1. View Dive Logs:
   - This option allows you to view all the existing dive logs
   in numerical order.

2. Add Dive Log:
   - Use this option to add a new dive log to the database.
   - You will be prompted to enter information such as the dive date,
   dive buddy name, and dive site name.
   - Dive time is to be entered in minutes and requires an integer input;
   - Dive depth is to be entered in meters and requires an integer input;
   - Starting and Ending air is to be entered in PSI
    and requires an integer input.
   - Ending Air value must be lower than Starting Air.
   - All fields are required to complete the log.


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
    print(Fore.CYAN + "Please scroll up to see all info" + Style.RESET_ALL)


def display_goodbye():
    """
    Function to quit program and display goodbye image and message
    """
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
    """
    Defines function to clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    """
    Function to display main menu options when called

    """
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
        print(Fore.RED + "Invalid option. Please try again."
              + Style.RESET_ALL)

    if running:
        input("Press Enter to go back to the Main Menu.\n")
        clean_up_terminal()


def main():
    display_logo()
    display_main_menu()


if __name__ == "__main__":
    main()
