# Scuba Dive Log


![Scuba Dive Log](documentation/scubadiveloggrab11.png)

*The link to [Scuba Dive Log](https://dive-log-9f66ea37cc55.herokuapp.com/)*

Scuba Dive Log is a Python terminal project designed to log users' scuba dive information. It allows divers to keep track of all their dives by storing useful information such as dive date, dive buddy, dive site name, dive depth (in meters), dive time (in minutes), and air consumed (in PSI).

PSI stands for Pounds per Square Inch which is an important unit of measurement used when scuba diving. It measures the amount of air pressure inside the cylinder that divers breathe from while underwater. Knowing how much air pressure there is in your scuba tank helps divers plan dives safely and accurately so that they can make the most out of their dives!

---
## Table of Contents

1. [Scuba Dive Log](#scuba-dive-log)
2. [How to use the program](#how-to-use-the-program)
3. [User Stories](#user-stories)
   - [First Time Visitor Goals](#first-time-visitor-goals)
   - [Frequent Visitor Goals](#frequent-visitor-goals)
4. [Features](#features)
5. [Flowchart](#flowchart)
6. [Database Structure](#database-structure)
7. [Technologies Used](#technologies-used)
   - [Languages](#languages)
   - [Frameworks/Libraries, Programs, and Tools](#frameworkslibraries-programs-and-tools)
8. [Bugs](#bugs)
9. [Testing](#testing)
10. [Validation](#validation)
11. [Deployment](#deployment)
   - [Git and GitHub](#git-and-github)
   - [Deployment to Heroku](#deployment-to-heroku)
12. [Future Enhancements](#future-enhancements)
13. [Credits](#credits)
14. [Acknowledgments](#acknowledgments)

## How to use the program:

1. Click on this *[link](https://dive-log-9f66ea37cc55.herokuapp.com/)* or copy and paste this text: `https://dive-log-9f66ea37cc55.herokuapp.com/` into your browser's address bar.
2. Once the page is loaded, click on 'RUN PROGRAM'.
3. Follow the instructions provided by the program.
4. Choose from various options available, such as viewing dive logs, adding dive logs, deleting dive logs, searching dive logs, reading instructions, learning about the program, or quitting.
5. When you are done, choose "Quit" and **send** the link to this program to your friends!

Link to the program: *[https://dive-log-9f66ea37cc55.herokuapp.com/](https://dive-log-9f66ea37cc55.herokuapp.com/)*

---
## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the purpose of the program so that I can learn more about it.
* As a First Time Visitor, I want to easily navigate through the program to find the content I need.
* As a First Time Visitor, I want to add and store my dive data.
* As a First Time Visitor, I want to find information about the developer and the program.

### Frequent Visitor Goals:
* As a Frequent User, I want to review my previous dive logs.
* As a Frequent User, I want to update my dive experiences and edit old logs.

---

## Features
  
- **When the program is loaded**
  - Users will see a logo and a main menu that explains the purpose of the program:
  
  ![loading Program](documentation/scubadiveloggrab11.png)


  - Shows the terminal menu with seven options:

    1. View Dive Logs;

    2. Add Dive Logs;
    
    3. Delete Dive Logs;

    4. Search Dive Logs;

    5. Instructions;

    6. About;

    7. Quit;

      ![loading Program](documentation/features/main_menu.png)

- **When the user chooses "View Dive Logs"**
  - The program displays the dive logs.

- **When the user chooses "Add Dive Log"**
  - The program shows a sub-menu with options to add various types of dive logs.

- **When the user chooses "Delete Dive Log"**
  - The program asks for the log's ID to delete it.

- **When the user chooses "Search Dive Logs"**
  - The program asks for specific criteria to search for dive logs.

- **When the user chooses "Instructions"**
  - The program displays instructions on how to use it.

- **When the user chooses "About"**
  - The program provides information about the program and the developer.

- **When the user chooses "Quit"**
  - The program shows a goodbye message and stops.

---

---

## Flowchart

The flowchart below represents the logic progression of the Scuba Dive Log application:

![FlowChart](documentation/firstflowchart.png)
![FlowChart](documentation/lucidflowchart.png)

## Database Structure

The Scuba Dive Log application uses Google Sheets to store and retrieve data. The application has one worksheet named "DiveLog" that stores all the data.

![database](documentation/googlesheetsdivelog.png)

The worksheet consists of seven columns: Dive Date, Dive Buddy, Dive Site Name, Dive Depth, Dive Time, Starting Air, and Ending Air. This structure allows the program to store and retrieve dive log data from the Google Sheets spreadsheet.
  

The ID column value is assigned automatically when a new divelog is added.

---
## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [datetime](https://docs.python.org/3/library/datetime.html) The datetime module supplies classes for manipulating dates and times.
- [os](https://docs.python.org/3/library/os.html) was used to clear the terminal before running the program.

- [copy](https://docs.python.org/3/library/copy.html) The copy module is used in the delete_dive_log() function. The copy.copy() function is used to create a shallow copy of the dive log list obtained from the Google Sheets spreadsheet. This allows the function to update the list of dive logs after deleting a log without modifying the original list.

##### Third-party imports:

- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [SnippingTool](https://snippingtoolfree.com/) was used to capture images for the README file.
- [Lucid Flow Chart](https://www.lucidchart.com/) was used to make a flowchart for the README file.
- [heroku.com](https://heroku.com/) was used to deploy the project.


---

## Bugs

Please refer to the [TESTING.md](TESTING.md) file for all bug related documentation.
---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test related documentation.

---
## Validation 

### PEP8

[PEP8CI](https://pep8ci.herokuapp.com/) app was used to lint the code.
It was helpful to edit with then copy the fixed code back into VS Code.
After a ropey start with many errors that gave me a fright initially, I got it down to no errors without too much hardship. Most of the issues involved having lines that had too many characters, white space, or wrong indents.

![pep8_validation](documentation/linterpass.png)
#   Deployment

## Git and GitHub

1. [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create GitHub public 
repository [divelog](https://github.com/kimatron/divelog). In template repository click on "use this template" --> "create new repository", 
choose repository name and click on the green button "Create repository from template".

2. Clone repository to your local machine using GitHub.
3. Use the following commands to add, commit and push changes:
    - git add .
    - git commit -m "Do something"
    - git push
    Also:
    - clear (to clear the terminal)
    - git status (to know if your app is up to date and your working tree is clean)

4. Ensure that all libraries and packages are listed in requirements.txt file.

5. When program is ready for further deployment, visit heroku.com website to deploy on heroku.

## Deployment to Heroku

1. Navigate to [https://heroku.com/](https://heroku.com/) and open dashboard. Then click the button "New" and select "Create new app" button.

2. Enter app name, choose region, and click on "Create app" button

3. The next step is to go to "Deploy" tab and then to "Deployment method" section to authorize and connect your GitHub account.

4. Upon successful connection, select main branch from repository.

5. Then go to "Settings" tab.

6. Next go to "Buildpacks" section. Add python and nodejs buildpacks. Order here is very important.

7. Next go to "Config Vars" section and add KEY "CREDS" - that matches your token name defined in python constant
 in [api/google_sheets_api.py] with value of your credentials token (copy all and paste).

8. Add key "PORT" with value "8000" and save changes.

6. Go back to "Deploy" tab. I initially used manually deploy, but you can also use automatic deploy. I had this set up, but I found it wasn't deploying the updated latest push for some reason. Maybe I'm just too impatient!

7. The link to my deployed app was shown on screen: https://dive-log-9f66ea37cc55.herokuapp.com//

## Future Enhancements

There are several future enhancements that can be made to improve the functionality and user experience of the Scuba Dive Log program:

- When I get time I will finish off adding and co-ordinating color to all text, make a more aesthetically pleasing background and make it functioning on mobile phones.

- Implement user authentication to allow multiple users to log in and manage their own dive logs. This would provide a more secure and personalized experience for users.

- Add the ability to edit existing dive logs. Currently, users can only add or delete dive logs. Allowing for edits would provide more flexibility in managing dive information.

- Improve the search functionality to allow for more advanced search options. For example, users could search for dive logs by a specific date range or dive depth range, making it easier to find specific dives.

- Implement more data validation to ensure that input values meet the required format and constraints. This would help prevent errors and ensure that the dive log data is accurate and consistent.

- Add a feature to add dive certification information / images of dive cert cards to store in the app.

- Calculate air consumed and document air consumption over time.

- Add additional statistics and data analysis features to provide insights into the user's dive history. This could include visualizations of dive data, such as charts or graphs, to help users analyze their dive patterns and progress over time.

- Allow users to export their dive logs to a CSV file for further analysis or sharing. This feature would enable users to extract their dive data and use it in other applications or share it with dive buddies or instructors.

These future enhancements would further enhance the functionality and usability of the Scuba Dive Log program, providing users with a more comprehensive and customizable experience.

---
## Credits
- Used [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template) template to start off project.
- Sourced some style code ideas for formatting long lines of code and adding color effectively:
[w3schools](www.w3schools.com),
[Stackoverflow](Stackoverflow.com),
[FreeCodeCamp](www.freecodecamp.org).
- Rewatched Love Sandwiches project from [Code Institute](www.codeinstitute.com) for inspiration on how to start setting up my site
- Used [TextKool](https://textkool.com/) to create Dive Log logo with Ascii generator.
- Read through README.md and TESTING.md of older projects to get template base of what information I needed to fill in for my documentation.
- Used [Asciiart](https://www.asciiart.eu/sports-and-outdoors/scuba) for the ascii scuba diver art in the goodbye message.

### Acknowledgments
- Thanks to [Viola](https://github.com/violaberg) for keeping me sane and providing advice and motivation at silly o clock in the morning when my eyes weren't working anymore and joining me for ANOTHER halloween hackathon in the middle of the project, just to add more stress to the mix :)
- And thanks to my mentor [Juliia](https://github.com/IuliiaKonovalova) for putting up with my "working best under time pressure" method of working and providing helpful advice and figuring out my bugs with her keen eye :)  
 