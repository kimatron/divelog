## Bugs

+ **Solved bugs**

When adding an invalid date the incorrect input wasn't notified until after three questions.

![Date Validation Bug](documentation/bugdatevalidation.png)

After pulling my hair out for about 28minutes I found the simple issue was I was calling three questions before validating the first one

![Date Validation Bug](documentation/bugfinddatevalidation.png)

Moving the 2nd and 3rd input below the date validation fixed the problem

![Date Validation Bug](documentation/bugdatevalidationfix.png)

- When trying to quit the program I encountered my first real life neverending infinity bug:

![Exit Infinity Bug](documentation/bugexitloop.gif)

Adding a simple exit() call fixed the problem.

- When adding a new dive, input called to enter Dive Buddy Name then Dive Site Name, but when entered correctly and calling on the view dive log functions, the information was recalled in the wrong order.

![Dive Buddy/Site Bug](documentation/bugdivesitemix.png)

- Looking at the spreadsheet I noticed the titles were in the wrong order, so just switching columns fixed the issue:

![Dive Buddy/Site Bug](documentation/bugsitefix1.png)
![Dive Buddy/Site Bug](documentation/bigsitefix2.png)

- The Yes/No query input was accepting any key responses, then when I tried to fix it the N response was not diverting back to the main menu

![y/n Bug](documentation/bugyesnoany.png)
![y/n Bug initial fix](documentation/bugyesnofix.png)
![y/n Bug fix](documentation/bugyesnonewfix.png)

- When showing an error on empty fields when adding dives, the error wasn't showing straight away because I was doing my validation together at the end of inputs in the function. Then with my initial fix, when the error showed it brought the user back to the start of the form to begin all over again. This would be a very frustrating user experience. 

![All fields required Bug](documentation/bugallfields.png)

* To fix it I added checks on each individual input.

![All fields required Bug](documentation/bugsearchrequiredfix.png)

- Changing names of files and folders in VScode did not take effect in GitHub, thus throwing errors in links to images in README and TESTING. I deleted from source in GitHub and uploaded again. I think the problem occurs when I change the name after pushing the added files, but I can't find a definitive answer as to why, but it is pretty frustrating!

## (almost) Unfixed bugs

- When deleting a dive log the program gives an option to delete another index or go back to the main menu.
It gives the correct error of invalid input for the first incorrect input, but then allows to go back to the main menu.
I don't think this is a big problem, but will fix it when I get a chance.

![Double input error bug](documentation/unfixedbug.png)


- In the delete log function, when an invalid option is entered twice in a row, the invalid error sign shows briefly and automatically displays all dive logs again. There is something wrong with the loop, that I will fix as soon as I get the chance. The function still works, it's just not as user friendly as I want it to be.

LAST MINUTE FIX!
Added an extra while True loop (line 50) to ensure that the program keeps prompting the user until a valid input ('y' or 'n') is provided for the question "Do you want to delete another dive log?"

Within the new while True loop, added an if statement (line 51) to check if the input is 'n'. If it is, the function returns to the main menu, effectively ending the execution of the delete_dive_log() function.

In the same if statement, added an elif statement (line 53) to check if the input is 'y'. If it is, the break statement is executed, which exits the inner while loop and continues with the execution of the outer while loop.

Added an else statement (line 56) to handle invalid inputs for the question "Do you want to delete another dive log?" If the input is neither 'y' nor 'n', the program prints an error message and continues to prompt the user until a valid input is provided.

## Mystery Bug
Twice when I clicked on my deployed link the deployed screen did not load properly. No code had been edited or changed for it to cause an error, by redeploying it on heroku it displayed correctly again. Hopefully it does not do this again when I am not working on it daily to notice.

![Double input error bug](documentation/divelognotworking.png)





# Manual testing of validation and functionalities

Testing of application functionalities and validations were done throughout the building process.

## Main menu

![Main Menu](documentation/scubadiveloggrab11.png)

Function used for inputs validation - def display_main_menu()

| What is being tested | Input  | Expected response | Result  |
|---|---|---|---|
|  Please select a number from 0 to 6 to continue | "any number not 0-6", "abc", "empty"   |Invalid Option - Try Again | Pass
|  Please select a number from 0 to 6 to continue | "1" | Valid input, call view_dive_logs fn  | Pass
|  Please select a number from 0 to 6 to continue | "2" | Valid input, call add_dive_log fn | Pass
|  Please select a number from 0 to 6 to continue | "3" | Valid input, call delete_dive_log fn | Pass
|  Please select a number from 0 to 6 to continue | "4" | Valid input, call search_dive_logs fn  | Pass
|  Please select a number from 0 to 6 to continue | "5" | Valid input, call display_instructions fn | Pass
|  Please select a number from 0 to 6 to continue | "6" | Valid input, call display_about fn | Pass
|  Please select a number from 0 to 6 to continue | "0" | Valid input, call goodbye fn | Pass

# View Dive Logs function

| Test Description                   | Test Data                                                             | Expected Result                  | Test Result |
| --------------------------------- | --------------------------------------------------------------------- | -------------------------------- | ----------- |
| Valid dive logs                    | Dive logs: [{'Dive Date': '2022-01-01', 'Dive Buddy Name': 'John',... | Dive logs displayed correctly    | Passed      |
| Empty dive log database            | Dive logs: []                                                         | "No dive logs found." displayed  | Passed      |
| Search database            | Dive logs: []                                                         | "No dive logs found." displayed  | Passed      |


## Add dive log function

Function used - add_dive_log() 

The function is used to validate Dive Date, Dive Buddy Name, Dive Site Name, Dive Depth (in metres), Dive Time (in minutes), Dive Starting Air (in PSI) and Dive Ending Air (in PSI). Dive Time, Dive Depth, Dive Starting Air and Dive Ending air all require integer inputs.

| Test Description                                       | Test Data                                                             | Expected Result | Test Result |
| ----------------------------------------------------- | --------------------------------------------------------------------- | --------------- | ----------- |
| Valid input                                            | Date: 2022-01-01<br>Dive Buddy: John<br>Dive Site: Test Site<br>...   | Dive log added successfully! | Passed      |
| Missing required fields                               | Date: 2022-01-01<br>Dive Buddy: John<br>Dive Site:                      | Error: All fields are required. | Passed      |
| Invalid date format                                    | Date: 2022-01-01 | Invalid date format. Please enter the date in YYYY-MM-DD format.    | Passed      |
| Invalid date format                                    | Date: 2092-01-01 | Invalid date format. Dive Log Date can not be in the future.    | Passed      |
| Invalid numeric input for dive depth                   | Dive Depth: abc | Invalid input. Please enter an integer.   | Passed      |
| Invalid numeric input for dive time                    | Dive Time: abc | Invalid input. Please enter an integer.   | Passed      |
| Invalid numeric input for dive time                    | Dive Time: -50 | Invalid input. Dive time must be postive integer.   | Passed      |
| Invalid numeric input and order for starting air       | Starting Air: abc | Invalid input. Please enter an integer. | Passed      |
| Invalid numeric input and order for ending air         | Ending Air: abc | Invalid input. Please enter an integer. | Passed      |
| Invalid Ending Air Higher Than Starting Air         | Ending Air: 9999 | Invalid input. Please enter number less than starting air. | Passed   


## Yes/No question

| Test Description                     | Test Data                         | Expected Result                                           | Test Result |
| ----------------------------------- | --------------------------------- | --------------------------------------------------------- | ----------- |
| Valid input - "y"                    | User input: "y"                   | Function proceeds with the desired action                  | Passed      |
| Valid input - "n"                    | User input: "n"                   | Function proceeds without taking the desired action       | Passed      |
| Invalid input - empty input          | User input: ""                    | Prompt for valid input displayed                           | Passed      |
| Invalid input - invalid characters   | User input: "123"                 | Prompt for valid input displayed                           | Passed      |



## Search dive log function

| Test Description                          | Test Data                                                             | Expected Result                      | Test Result |
| ---------------------------------------- | --------------------------------------------------------------------- | ------------------------------------ | ----------- |
| Valid search query - match found          | Search query: "Test Site"                                              | Matching dive logs displayed         | Passed      |
| Valid search query - no match found       | Search query: "Nonexistent Site"                                       | "No matching dive logs found."       | Passed      |
| Invalid search query - empty input        | Search query: ""                                                       | "No matching dive logs found."       | Passed      |
| Invalid search query - invalid characters | Search query: "!@#$%"                                                  | "No matching dive logs found."       | Passed      |
| Search again - valid input (Y)            | User input: "Y"                                                        | Prompt for new search query displayed | Passed      |
| Search again - valid input (N)            | User input: "N"                                                        | Function returns                      | Passed      |
| Search again - invalid input              | User input: "Invalid"                                                  | Prompt for valid input displayed      | Passed      |

## Delete Dive Log function

| Test Description                                 | Test Data                        | Expected Result                                | Test Result |
| ----------------------------------------------- | -------------------------------- | ---------------------------------------------- | ----------- |
| Valid input - delete a dive log                  | User input: 2                    | Dive log at index 2 is deleted                  | Passed      |
| Invalid input - non-integer value                | User input: 'abc'                | Error message displayed, no dive log is deleted | Passed      |
| Invalid input - out of range index               | User input: 10                   | Error message displayed, no dive log is deleted | Passed      |
| Valid input - cancel dive log deletion           | User input: 'n'                  | Dive log deletion canceled, no dive log is deleted | Passed      |
| Valid input - delete a dive log and delete another| User inputs: 2, 'y', 'y'         | Dive log at index 2 is deleted, and dive index is called to delete another | Passed      |
| Valid input - return to main menu                 | User input: 'm'                  | Returns to the main menu, no dive log is deleted | Passed      |


##  clean_up_terminal() function

| Test Description                    | Expected Result       | Test Result |
| ---------------------------------- | --------------------- | ----------- |
| Running on Windows                  | Clear the terminal    | Passed      |


# Exit function

| Test Description                 | Expected Result                                | Test Result |
| ------------------------------- | ---------------------------------------------- | ----------- |
| Display goodbye message          | Goodbye message and ASCII art are printed      | Passed      |
| Exit program                     | Program terminates                             | Passed      |

# Python Linter PIP8
Entire run.py final code ran through Python Linter and passed with no errors.

![Main Menu](documentation/updatedlinterpass.png))