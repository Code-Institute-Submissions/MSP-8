# Testing 

The following sections are the results of the testing throughout the software development lifecycle for MSP-2. This information has been included in a separate document in order to keep the README document uncluttered.

Due to the size and nature of this project, while there will be rounds of testing, instead of distinct testing phases (ie unit, system etc)

## Functionality Testing:
Each round of testing will contain the following information:
        - Date Testing was conducted
        - Environment on which testing was conducted (MVP, Pre-Deployment, Post Deployment)
        - Functionality that has been developed
        - Test results / comments
        - Remaining planned functionality still to be developed
        - Evidence of testing (GIF / Screen capture)

### Round One - Testing on MVP
10/07/2021 
        Functionality available:
                Basic logic flow for three pathways to the "dragon"
                Functions with basic text at each step
                End game & retry functions
                Dragon with placeholder responses

        Test Results:
                There are no broken functions stopping the user from proceeding
                Error were discovered surrounding the character length of some rows
                PEP8 validation was a pass
                Occational indentation error

        Planned Functionality to be developed:
                - Varying Game_over functions for Quit / Successful and Death by Misadventure
                - ASCI type artwork
                - Changing colours
                - Obtaining User name and using it within other functions

![deeperdesertevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/deeper_desert_screen.PNG")
![deeperforestevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/deeper_forest.PNG")
![desertquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/desert_quit_screen.PNG")
![desertevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/desert_screen.PNG")
![dragonquestionsquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/dragon_question.PNG")
![dragonevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/dragon_screen.PNG")
![forestevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/forest_screen.PNG")
![gorgeevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/gorge_screen.PNG")
![oasisevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/oasis_screen.PNG")
![oceanquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/ocean_quit.PNG")
![oceanevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/ocean_screen.PNG")
![pondquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/pond_screen.PNG")
![startquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/start_quit_screen.PNG")
![startevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/start_screen.PNG")
![PEP8evidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/pep8.PNG")
![testevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/test_results_one.PNG")



### Round Two - Testing on MVP
17/07/2021 
        Functionality available:
                Basic logic flow for three pathways to the "dragon"
                Functions with basic text at each step
                End game & retry functions
                Dragon with placeholder responses
                ASCI imagry
                Obtaining user/player Name
                Varying Game_over functions for Quit / Successful and Death by Misadventure
                Different colours for text

        Test Results:
                There are no broken functions stopping the user from proceeding
                ASCI imary is appearing as expected (with the exception of color)
                Colour has not been applied to all applicable screens as per the evidences below

        Planned Functionality to be developed:
                Using user/player within other functions
        
        Evidence:

![deeperdesertevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/deeper_desert_error.PNG")
![deeperforestevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/deeper_forest_error.PNG")
![dragonevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/dragon_error.PNG")
![gamecompleteevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/game_complete_error.PNG")
![gorgeeevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/gorge_error.PNG")
![oasisevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/oasiss_error.PNG")
![oceanevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/ocean_error.PNG")
![pondevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/pond_error.PNG")

![startevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/start_screen_invalid.gif")
![startquitevidence](url"https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/start_screen_quit.gif")

### Round Three - Testing on Final Product prior to deployment
19/06/2021
        Functionality available:
                Basic logic flow for three pathways to the "dragon"
                Functions with basic text at each step
                End game & retry functions
                Dragon with placeholder responses
                ASCI imagry
                Obtaining user/player Name
                Varying Game_over functions for Quit / Successful and Death by Misadventure
                Different colours for text
                Use of user/player name throughout the various functions
        Test Results:


        Planned Functionality to be developed:
                Not applicable


![evidence]()


## Compatability testing:

As this application is primarily a command line program, it has been developed with Desktop as the primary access method.
The python application (run.py file) has been tested on MAC, Windows and linux.


## User Acceptance Testing:

Due to the size and timelines of this project, there will not be a structured Alpha/Beta stage of UAT. Instead, a selection of volunteers will conduct a time boxed exploratory session. After which feedback will be collated and transformed into bugs, improvements or new features.

The following is the feedback provided from the end users from their exploratory test session:
 - 

## Performance Testing:
The following evidence are the results from the performance speed test conducted on the deployed site:

![performance]()

## Production Shakedown Pre Submission

Once the web application had been deployed the python code was passed through the official PEP8 validator:

![pep8validator]()

All steps/pages have been visually inspected to ensure all information has been correctly populated and loaded.

### Unfixed bugs

- 