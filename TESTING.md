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
                - Basic logic flow for three pathways to the "dragon"
                - Functions with basic text at each step
                - End game & retry functions
                - Dragon with placeholder responses

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

![deeperdesertevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/deeper_desert_screen.PNG)
![deeperforestevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/deeper_forest.PNG)
![desertquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/desert_quit_screen.PNG)
![desertevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/desert_screen.PNG)
![dragonquestionsquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/dragon_question.PNG)
![dragonevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/dragon_screen.PNG)
![forestevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/forest_screen.PNG)
![gorgeevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/gorge_screen.PNG)
![oasisevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/oasis_screen.PNG)
![oceanquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/ocean_quit.PNG)
![oceanevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/ocean_screen.PNG)
![pondquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/pond_screen.PNG)
![startquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/start_quit_screen.PNG)
![startevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/start_screen.PNG)
![PEP8evidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/pep8.PNG)
![testevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%201/test_results_one.PNG)



### Round Two - Testing on MVP
17/07/2021 

        Functionality available:
                - Basic logic flow for three pathways to the "dragon"
                - Functions with basic text at each step
                - End game & retry functions
                - Dragon with placeholder responses
                - ASCI imagry
                - Obtaining user/player Name
                - Varying Game_over functions for Quit / Successful and Death by Misadventure
                - Different colours for text

        Test Results:
                There are no broken functions stopping the user from proceeding
                ASCI imary is appearing as expected (with the exception of color)
                Colour has not been applied to all applicable screens as per the evidences below

        Planned Functionality to be developed:
                Using user/player within other functions
        

        Evidence:

![deeperdesertevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/deeper_desert_error.PNG)
![deeperforestevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/deeper_forest_error.PNG)
![dragonevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/dragon_error.PNG)
![gamecompleteevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/game_complete_error.PNG)
![gorgeeevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/gorge_error.PNG)
![oasisevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/oasiss_error.PNG)
![oceanevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/ocean_error.PNG)
![pondevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/pond_error.PNG)

![startevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/start_screen_invalid.gif)
![startquitevidence](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%202/start_screen_quit.gif)

### Round Three - Testing on Final Product prior to deployment
19/06/2021

        Functionality available:
                - Basic logic flow for three pathways to the "dragon"
                - Functions with basic text at each step
                - End game & retry functions
                - Dragon with placeholder responses
                - ASCI imagry
                - Obtaining user/player Name
                - Varying Game_over functions for Quit / Successful and Death by Misadventure
                - Different colours for text
                - Use of user/player name throughout the various functions
        Test Results:
                While there are warning messages displaying on the PEP8 python checker, these additional whitespaces are required to enable the ASCI imagry to display correctly.
                All lines within the python run/py file are under 80 characters
                The final planned happy path logic works without errors
                Each input screen handles the user inputting the quit option
                Each input screen handles the user inputting an invalid input
                Dragon will only allow 3 questions before ending the game
                
        Planned Functionality to be developed:
                Not applicable all planned functionality has been implemented


![pythonvalidatorpart1](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/pep8part1.PNG)
![pythonvalidatorpart2](https://github.com/Sphere42/MSP-3/blob/main/assets/readme/pep8part2.PNG)

![deeperdesert](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/deeperdesertinvalidquit.gif)
![desertinvalidquit](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/desertinvalidquit.gif)
![dragon1](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/dragon1.gif)
![dragon2](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/dragon2.gif)
![dragon3](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/dragon3.gif)
![dragon4](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/dragon4.gif)
![forest](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/forest.gif)
![forest2](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/forest2.gif)
![full](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/full.gif)
![fullforest](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/fullforest.gif)
![fullocean](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/fullocean.gif)
![gorge](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/gorge.gif)
![ocean](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/ocean.gif)
![pond](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/pond.gif)
![ostartinvalidquit](https://github.com/Sphere42/MSP-3/blob/main/assets/testing/Round%203/startinvalidquit.gif)

## Compatability testing:

As this application is primarily a command line program, it has been developed with Desktop as the primary access method.
The python application (run.py file) has been tested on MAC, Windows and linux.


## User Acceptance Testing:

Due to the size and timelines of this project, there will not be a structured Alpha/Beta stage of UAT. Instead, a selection of volunteers will conduct a time boxed exploratory session. After which feedback will be collated and transformed into bugs, improvements or new features.

The following is the feedback provided from the end users from their exploratory test session:
 - 

## Performance Testing:
Performance testing was not conducted on this site as the web application GUI was developed by the college.


## Production Shakedown Pre Submission

Once the web application had been deployed the python code was passed through the official PEP8 validator:

![pep8validator]()

All steps/pages have been visually inspected to ensure all information has been correctly populated and loaded.

### Unfixed bugs

- 
