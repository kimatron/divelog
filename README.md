# Scuba Dive Log

![Responsive Mockup](documentation/scubadivelogscreen.png)

*The link to [Scuba Dive Log](https://dive-log-9f66ea37cc55.herokuapp.com/)*

Scuba Dive Log is a Python terminal project whose primary purpose is to log users scuba dive information so that they can keep track of all their dives. It will store useful information that divers like to keep track of, such as:
* Dive Date
* Dive Buddy
* Dive Site Name
* Dive Depth (in meters)
* Dive Time (in minutes)
* Air Consumed (in PSI or bar)


---

## How to use program:

  1. Click this *[link](https://dive-log-9f66ea37cc55.herokuapp.com/)* or copy this text: `https://dive-log-9f66ea37cc55.herokuapp.com/` and paste it in your browser's address bar.
  1. As soon as the page is loaded, click 'RUN PROGRAM'.
  1. Introduce yourself to the program.
  1. Read the Instructions
  1.
  1. 
  1. When you are done dreaming of dives of yore, choose "Quit" and **send** the link to this program to your friends!

  Link to the program: *https://dive-log-9f66ea37cc55.herokuapp.com/*

---
## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the program's primary purpose so that I can learn more about this program.
* As a First Time Visitor, I want to navigate through the program easily so that I can find the content.
* As a First Time Visitor, I want to be able to add and store my dive data.
* As a First Time Visitor, I want to see information about the developer and the program.

### Frequent Visitor Goals:
* As a Frequent User, I want to review my previous dive logs
* As a Frequent User, I want to update my new dive experiences and edit old ones.

---

## Features
  
  - **When the program is loaded**

  The user can see a logo and a main menu which will let the user know what the
  program is for:
  
  ![loading Program](documentation/features/welcome_message_name.png)

  - **When the user types a name.**

  - Sends personal greetings and short instruction on the next step;

  - Shows the terminal menu with seven options:

    1. View Dive Logs;

    2. Add Dive Logs;
    
    3. Delete Dive Logs;

    4. Search Dive Logs;

    5. Instructions;

    6. About;

    7. Quit;

      ![loading Program](documentation/features/main_menu.png)

  The user can manipulate the terminal menu with the arrow keys to choose an option and the enter key to confirm the choice.

  - **When the user chose "View Dive Logs"**

  

  ![loading Program](documentation/features/rules.png)

  - **When the user chose "Add Dive Log"**

  The program will show the sub-menu with the following options to choose from:

  

  ![loading Program](documentation/features/sub_menu.png)

  Here the user can choose which story is preferable to play or go back to the main menu.

- **When the user chose "Delete Dive Log**

  

  ![loading Program](documentation/features/typing_words.png)

- **When the user chose "Search Dive Logs**


  ![loading Program](documentation/features/after_input.png)
  ![loading Program](documentation/features/story.png)

 - **When the user chose "Instructions**

 - **When the user chose "About**

  - **When the user chose "Quit"**


  The user will see a goodbye message, and the program will be stopped.

  ![loading Program](documentation/features/goodbye_message.png)

---

## Flowchart

The flowchart represents the logic of the application:
![FlowChart](documentation/firstflowchart.png)
  ![FlowChart](documentation/flowchart_divelog.png)



---
## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program.
##### Third-party imports:

- [NLTK Package](https://www.nltk.org/) was used in order to be able to work with pattern package.
- [Pattern Package](https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/) was used to pluralize nouns where it is needed.
- [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/) was used to implement the menu.
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [GIMP](https://www.gimp.org/) was used to make and resize images for the README file.
- [Draw.io](https://www.lucidchart.com/) was used to make a flowchart for the README file.
- [render.com](https://render.com/) was used to deploy the project.


---

## Bugs

+ **Solved bugs**


1. The function ```choosing_article(word)``` did not give the correct article if the noun was uncountable.

    - *Solutions:* rewrote function with using args; rather than checking only the beginning of the word, it checks all arguments and presents the correct  article

     ```python
    def choosing_article(*words):
        """
        Checks which article to use before the word and place the article before it
        """
        # Checks if the last word is countable.
        #If it is uncountable, returns all words
        if words[-1] in uncountable_nouns:
            return ' '.join(words)
        else:
            # Checks if the word starts with a vowel, adds 'an' before the word
            if words[0][0] in dictionary_letters['vowels']:
                return 'an ' + ' '.join(words)
            # Otherwise, adds 'a' before the word
            else: 
                return 'a ' + ' '.join(words)
      ```

1. Conjugate function did not work due to the RunTimeError raised by Python.

    - *Solutions:* add function which runs the function at first raising this error and then passes this error.

     ```python
    def run_the_time_error():
        """
        Prevent "RuntimeError: generator raised StopIteration"
        The package has raised StopIteration that was missed in python earlier versions.
        Thus, it had worked before Python version 3.7 was introduced.
        Since the package has not been updated since August 2018, it raises the error and stops the app.
        "PEP 479 is enabled for all code in Python >= 3.7, meaning that StopIteration exceptions raised
        directly or indirectly in coroutines and generators are transformed
        into RuntimeError exceptions."
        Link to this change:
        https://docs.python.org/3/whatsnew/3.7.html#changes-in-python-behavior
        """
        try:
            conjugate(verb = '', tense = PAST)
        except RuntimeError:
            pass

    run_the_time_error()
    ```


1. Pattern package could not spot the uncountable nouns, and as a result, pluralized uncountable nouns automatically.

    - *Solutions:* created list of uncountable nouns and a function which checks whether the word is countable or uncountable at first. Then if it is countable, pluralize this word.

    ```python
    def plural_noun(noun):
    """
    Checks whether the noun is countable or not and transform into plural if it's countable
    This function is needed to prevent the pluralization of uncountable nouns bt pattern package.
    """
    # Checks if the noun is uncountable; if it is, returns the nouns
    if the noun in uncountable_nouns:
    if noun in uncountable_nouns:
        return noun
    # Otherwise, pluralize noun with the patterns package
    return pluralize(noun)
    ```


+ **Unsolved bugs**

    - 

---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test related documentation.

---
## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://dive-log-9f66ea37cc55.herokuapp.com/)
### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/IuliiaKonovalova/madlib_with_python).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/IuliiaKonovalova/madlib_with_python)

  1. Install Python module dependencies:
     
      1. Navigate to the folder madlib_with_python by executing the command:
      - `cd madlib_with_python`
      1. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`
      1. *Note:* If you are located in China ![China](https://www.countryflags.io/cn/flat/32.png) or any other country with restricted internet access, you may need to add the following code in order to be able to use the nltk package.
      
       - For example:

        ```python
        nltk.set_proxy('127.0.0.1:41091')
        ```
      - To set the proxy, you need to open setting in preferred VPN, find Server address and HTTP/HTTPS Proxy Port joining them by colons as it is shown in the example above:
      ![Settings VPN](documentation/deployment/settings_vpn.png)

      

**The app was initially deployed to Heroku then moved to Render since Heroku has removed its free tier services from November 29 2022**

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/deployment/new_heroku_app.png)

  1. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

      - ![Deployment Method](documentation/deployment/deployment_method.png)

  1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link_to_github.png)

  1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/settings_tab.png)

  1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add_buildpack.png)

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add_python_and_node_js.png)

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/reveal_config_vars.png)

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy_branch.png)

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/deploying_branch.png)

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view_app.png)


### To deploy the project to Render so it can be run as a remote web application:

Link to the deployed application on Render: [The Maddest Madlib](https://the-maddest-madlib.onrender.com)

1. Create a new Render account if you don't already have one here [Render](https://render.com/).

2. Create a new application on the following page here [New Render App](https://dashboard.render.com/), choose **Webserver**:

    - ![New Render App](documentation/deployment/render_new_web_service.png)

3. Select the GitHub option and connect the application to the repository you created.

    - ![GitHub Option](documentation/deployment/render_configure_github_account.png)

4. Search for the repository you created and click "Connect."

    - ![Connect to GitHub](documentation/deployment/render_connect_repository.png)

    - ![Connect to GitHub](documentation/deployment/render_connect_repository_connect.png)

5. Create name for the application

    - ![Create Application Name](documentation/deployment/render_create_name.png)

6. Select the region where you want to deploy the application.

    - ![Select Region](documentation/deployment/render_select_region.png)

7. Select branch to deploy.

    - ![Select Branch](documentation/deployment/render_select_branch.png)

8. Select environment.

    - ![Select Environment Variables](documentation/deployment/render_select_environment.png)

9. Render build command: `pip3 install -r requirements.txt && npm install`

    - ![Render Build Command](documentation/deployment/render_build_command.png)

10. Render start command: `node index.js`

    - ![Render Start Command](documentation/deployment/render_start_command.png)

11. Select Free plan.

    - ![Select Free Plan](documentation/deployment/render_payment_info.png)

12. Click on "Advanced" settings.

    - ![Advanced Settings](documentation/deployment/render_advanced_settings.png)

13. Add the following environment variables:

    - Key: PORT Value: 8000
    - Key: PYTHON_VERSION Value: 3.10.7

    - ![Add Environment Variables](documentation/deployment/render_advanced_settings_variables.png)

14. Click "Create Web Service."

    - ![Save Web Service](documentation/deployment/render_create_web_service.png)

15. Wait for the completion of the deployment.


---
## Credits
- Used [Code Institute](https://github.com/Code-Institute-Org/ci-full-template) template to start off project.
- Sourced some style code ideas for adjusting photo size and layout from various sources online:
[w3schools](www.w3schools.com),
[Stackoverflow](Stackoverflow.com),
[FreeCodeCamp](www.freecodecamp.org).
- Rewatched Love Sandwiches project from [Code Institute](www.codeinstitute.com) for inspiration on how to start setting up my site
- Used [TextKool](https://textkool.com/) to create Dive Log logo with Ascii generator.
- 

### Acknowledgments
- Thanks to Viola for keeping me sane and providing advice at silly o clock in the morning when my eyes weren't working anymore and joining me for a hackathon in the middle of the project, as if we didn't have enough to keep us awake at night :)
- And thanks to my mentor [Juliia](https://github.com/IuliiaKonovalova) for not ignoring me and jumping in to answer all my annoying questions whenever she was asked :)  
 