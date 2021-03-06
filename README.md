# Choose your own adventure 

The purpose of Milestone Project 3 is to create a a text based choose your own adventure game, using python

# Project Summary

The Project will enable a user to:
- Partake in a mini adventure game
- Manipulate the direction of the story line via manual input
- Be entertained with imagry and jokes

## Benefits and Rational

Such an application will:
- Provide an entertaining game for the user to play
- The application will use imagry and jokes to amuse the user

## User Stories

Below is a high-level list of User Stories for the purposes of development, testing and delivery.

Business Case User Stories:

- As a User I want to be able to deploy and play the command-line application easily
- As a User I want to be able to navigate throughout the story with ease
- As a User I want all errors clearly explained and corrective actions available
- As a User I want all invalid inputs handled correctly and have the ability to proceed
- As a User I want the adventure to have a clear begining, middle, and ending
- As a User I want to be able to clearly determine when each step starts/finish
- As a User I want the ability to quit the game at any stage
- As a User I want the ability to know when input is required

Functional Developer Stories:

-	As a Developer I want to ensure the command-line application python code passes through the official validator without faults or errors
-	As a Developer I want to ensure all intended functionality works as per critial project objectives
-	As a Developer I want to ensure that all code means the minimum standards for readability as per PEP8
-	As a Developer I want to ensure the command-line application is responsive to user interaction
- As a Developer I want to ensure the command-line application handles incorrect user Input
-	As a Developer I want to ensure there are details (wireframes and final text sections) within the README document
-	As a Developer I want to ensure the web application meets accessibility guidelines
-	As a Developer I want to be able to easily deploy this command-line application to the cloud as per the Code Institutes requirements
- As a Developer I want to ensure Github is used for version control of the developing code
- As a Developer I want to utilise ASCI imagry to enhance the user experience

*Interpreted from the Assignment document*


# Functional Requirements Scope

## Design Consistancies

The following is a list of design aspects that must be maintained throughout the command-line application. 

The command-line application must be clear and concise. It should display, at a minimun:
- Print a message/image upon each user input
- Change the next step of the story based on user input
- Show a message if incorrect input has been entered
- Lead the user through a maze of steps that either
        - "meet the Dragon"
        - force a dead end
        - allow the user to quit
- Once at "the Dragon", allow the user to ask up to three questions
- Generate a random response to each question asked of the dragon
- If the user attempts to ask more then three questions, "the Dragon" will get angry and end the game
- The ability to quit the game at any stage by pressing the allocated quit option
- Handle any invalid user input gracefully and allow the user to continue

The following is a rough wireframe of the prdicted logical flow of the program

![initial logic concept](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/Logic%20Flow.PNG)

Each step will have the following options for the user:
- A step to progress along the story line
- A step that will end the game in a humourous way
- An option to quit the game
- An option to re-enter choice if invalid input is entered

# Final/Existing Feature Outcomes
The final command-line application happy path logic will be as follows:

![finallogic](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/happypath.PNG)

The final game will appear as follows:

![finalmultiview](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/multidevice.PNG)

# Future Features to be Implemented
      - Additional steps to extend the game
      - Additional options to the existing screens
      - Additional responses from the Dragon
      - Option to collect a weapon, maybe defeat the Dragon
      - Create an alternate ending
      - Further use of the users name throughout the various screens
      - Pull the ASCI images fromm an external file to remove "warnings" from PEP8 validator
      - Place limitations on the invalid user entry

# Testing 

Full details and evidence of testing conducted throughout the software development life cycle of this project will be maintained in a seperate document called testing.md

## Production Shakedown Pre Submission

Once the command-line application had been deployed the Python code was passed through the official PEP8 code validator
There are no errors identified within the code.
All warning messages are due to the ASCI imagry implemented within the project. A white space is required on rows that end with \ or /, without which, the rows would merge and the image would not display correctly.

![finalmultiview](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/pep8final.PNG)

All functions have been manually selected to ensure all information has been correctly populated and displayed


### Unfixed bugs

- Colours are not appearing as bold within the mock terminal as they are within a normal system terminal.
        - This will require changing the node.js code that formed part of the initial college template and therefore will not be corrected prior to submission

# Deployment Process

## Direct Deployment to Heroku

The site was deployed using Heroku. 

The steps to deploy are as follows: 

1. Ensure that the project has the correct content within the requirements.txt document by running the following commands in the IDE terminal

![requirements](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/1requirementsdoc.PNG)

2. Once the code is present and up to date, go to the Heroku website (https://www.heroku.com/). If not already signed up for a free account, please do so.

3. Once the Heroku Dashboard, select the option for New App, (note you can have up to five applications live with a free heroku account)

![createapp](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/2createapp.PNG)

4. This will display a page where you will need to give the project a name, and choose your region

![nameregion](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/3nameregion.PNG)

5. Once successful the project dashboard will display

![homepage](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/4homepage.PNG  )

**Note**: As this project does not make any API calls there is no requirement to add an authorisation key

6. Next you will need to tell the Heroku platform what Buildpacks are required, this is done in the Buildpack section on the settings screen

![settingsbp](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/5settingsbp.PNG)

7. For this project you will need both Python and Nodejs (individually added in that order)

![bppython](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/6bppython.PNG)
![bpnodejs](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/6bpnodejs.PNG)

8. Now, it is time to deploy the project. To do this, select the deployment tab and choose Github

![deploytab](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/8deploytabno%20auth.PNG)

9. Search for your repository, and select the correct match

![connect](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/9searchconnect.PNG)

10. Deploying to Heroku can be done one of two ways: 
- Automatically, which will mean the project will be with the latest code available each time it is loaded
- Manually, which will build the application as per the code available at the time of build. Any changes to the repository will not be added unless the manual build request is utilised again.

![deployment](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/10deployoption.PNG)

11. Success. Select the view option to see your live project

![success](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/11success.PNG)


The deployment link for this web apllication is: https://adventure-dragon.herokuapp.com/

![final](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/final.PNG)

## Copying the Code

Firstly, please remember that plagiarism is not only unprofessional, but illegal. Please feel free to utilise this code as a reference/learning material and credit the original source.

To obtain a copy of the code for this project, complete the following steps:

- Go to the code page of the project
  ![copy1](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/copy1.PNG)


- Select the "code" buttom in the top right hand corner

  ![copy2](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/copy2.PNG)

- From here the project code can either be
       Downloaded as a ZIP file
       Open with GitHub Desktop (if you have downloaded the app)
       Open with Visual Studio (if you have a copy of the program)


# Credits 

This project could not have been created without the following:

## Code Guidance
- Dragon response generation is loosely based on the magic 8-ball code located here
        https://www.w3resource.com/projects/python/python-projects-5.php

## API

Not applicable for this project

## Media

ASCI imagry
- https://www.asciiart.eu/

## Python Libraries

random
- Used to randomise the response that is printed by the dragon

time
- Used to implement the breaks that slow down the information being presented to the user

termcolor (cprint)
- Used to implement various text colours


## Development/Testing Validators

GitPod IDE
- https://gitpod.io

Python checker.
- http://pep8online.com/

Python formatter
- https://codebeautify.org/

Reduce picture size without effecting quality
- https://tinypng.com

GIFs for test evidence were created using ScreentoGif
- https://www.screentogif.com/

## Additional Thanks

Independant Reviewers: Tom Walsh, Daragh Curtis, 

Mentor: Felipe Souza Alarco
