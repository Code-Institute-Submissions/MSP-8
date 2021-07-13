import random
import time


# The following function is the initial step of the journey

def start():
    print('\nSo, you seek the wisdom of the Dragon to answer your questions?')
    print('\nThe journey is long and arguous, but rewarding!')
    print('To begin, you walk down a long, dark corridor')
    print('At the end you are faced with three doors')
    print('Which do you choose? (1, 2 or 3)')
    print('\n 1). Bright Yellow door to the left')
    print('2). Deep Green door directly ahead')
    print('3). Brilliant Blue door to the right')
    print('0). Runaway while you can coward......')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')

    # Validation and display surrounding invlaid character

    while answer not in ['1', '2', '3', '0']:
        print('Ah here, You just run into the wall,')
        print('How about you try using a door...')
        answer = input('>')
    if answer == '1':

        # lead the User into the desert adventure pathway

        desert()
    elif answer == '2':

        # lead the User into the forest adventure pathway

        forest()
    elif answer == '3':

        # lead the User into the ocean/water adventure pathway

        ocean()
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over('Then what are you doing here... get lost!!!')


# FIRST step (desert journey) in the yellow door/desert pathway

def desert():
    print('\nYou have chosen the yellow door')
    print('\nAll other doors disappear as you reach out for the door handle')
    print('As soon as the door opens, you are hit by a blast of heat.')
    print('You are in the middle of the desert.')
    print('Which do you choose? (1, 2 or 0)')
    print('1). Head straight into the dunes')
    print('2). Turn right and hope to find an end to this heat')
    print("0). Nah, I'm out, I need Air conditioning")

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('I know you are hot and tired, but you need to make a choice')
        answer = input('>')
    if answer == '1':

        # Head straight into the dunes result =head further

        deeper_desert()
    elif answer == '2':

        # Turn right and hope to find an end to this heat

        game_over('''There is no end to this heat.
        You end up lost in the expanse of sand,
        looks like you won't be seeing the Dragon today.''')
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("Leaving so soon... Fine chicken out why don't you...")


# SECOND step (deeper into desert journey) in the yellow door/desert pathway

def deeper_desert():
    print('\nAfter stumbling forward for miles in hot sand,')
    print('\nyou think you see an oasis off in the distance')
    print('Do you: (1, 2 or 0)')
    print('1). Turn towards the oasis and hope that it is real')
    print('2). Convince yourself that you are hallucinating and keep going')
    print('0). Run away')

    # Accept user input,allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('''I know you are hot and sweaty,
        but moving forward if the only way to go!''')
        answer = input('>')
    if answer == '1':

        # Turn towards the oasis and hope that it is real result =move forward

        oasis()
    elif answer == '2':

        # Convince yourself... = Game Over

        game_over('''What are you, Crazy?
        Like for real, who would choose the desert over an oasis!''')
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("Oooooo, Look who can't take the heat......")


# THIRD step (oasis step the desert journey) in the yellow door/desert pathway

def oasis():
    print('\nUpon Reaching the oasis you find relief')
    print('      in the shade of the tree branches')
    print('A short way into the oasis you see a small pond')
    print('Do you: (1, 2 or 0)')
    print('1). Have a drink before continuing into the desert')
    print('2). Dive in and enjoy a swim in the cool water')
    print('0). Run away')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('What? Did you fall asleep under a tree? Make a choice already')
        answer = input('>')
    if answer == '1':

        # Have a drink before continuing into the desert result = Game Over

        game_over('''Did you hit your head or something,
        why would you choose the desert over a swim''')
    elif answer == '2':

        # Dive in and enjoy a swim in the cool water result = move forward

        pond()
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("Ooooo, Look who can't take the heat.....")


# FOURTH step (deeper into desert journey) in the yellow door/desert pathway

def pond():
    print('\nWhile swimming you notice a small cave within the shallows')
    print('Do you: (1, 2 or 0)')
    print('1). Take a deep breath and dive into the unknown')
    print('2). Keep swimming and forget about the cave')
    print('0). Run away')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print("This isn't like the beer advert,")
        print("there is no wildcard 'Option C'")
        answer = input('>')
    if answer == '1':

        # Take a deep breath and dive into the unknown result = move forward

        dragon()
    elif answer == '2':

        # Keep swimming and forget about the cave result = Game Over

        game_over('''The Cave is just way too much adventure for you,
        Instead you abandon your quest and live out your days in the oasis''')
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over('So close and yet so far......')


# FIRST step (forest journey) in the green door/forest pathway

def forest():
    print('\nYou have chosen the green door')
    print('\nAll other doors disappear as you reach out for the door handle')
    print('After opening the door you find yourself...')
    print('in the middle of a tropical forest')
    print('Which do you choose? (1, 2 or 0)')
    print('1). Try to forge a path forward deeper into the undergrowth')
    print('2). Climb the biggest tree you can find, for a better view')
    print('0). Ew, mosquitoes')

# Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('There is no going back now, make a choice, forward or up.')
        answer = input('>')
    if answer == '1':

        # Try to forge a path forward... = move forward

        deeper_forest()
    elif answer == '2':

        # Climb the biggest tree you can find... = Game Over

        game_over('''The view from the top of the tree is amazing.
        Forest as far as the eye can see.
        Too bad the branch broke and you fell to the ground''')
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("Leaving so soon... Fine chicken out why don't you...")


# SECOND step (finding the gorge) in the green door/forest pathway

def deeper_forest():
    print('\nYou forge a path forward throw the thick undergrowth')
    print('\nEventually you reach a large gorge')
    print('You notice some vines that hang across the gap')
    print('Do you? (1, 2 or 0)')
    print('1). Swing across like Tarzan')
    print('2). Walk along the edge to find a safer way across')
    print('0). Nope, Heights are just way to much')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('Seriously dude, make a choice')
        answer = input('>')
    if answer == '1':

        # Swing across like Tarzan result = Game Over

        game_over('''What the frell. This is not a movie.
        How could you possibly think you could swing on a vine''')
    elif answer == '2':

        # Walk along the edge to find a safer way across = Move Forward

        gorge()
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("So I guess you don't need the Dragon's answers")


# THIRD step (crossing the gorge) in the green door/forest pathway

def gorge():
    print('\nYou walk along the edge until the sun is low in the sky')
    print('Just as you are about to give up you see a rope bridge ahead')
    print('Do you? (1, 2 or 0)')
    print('1). Carefully, but quickly, cross the rope bridge')
    print('2). The rope bridge looks flimsy,')
    print('    cotinue along the edge of the gorge')
    print('\n0). Got a problem with heights do ya princess?')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('invalid entry needed')
        answer = input('>')
    if answer == '1':

        # Carefully, but quickly, cross the rope bridge result = Game Over

        game_over('''You seriously thought this old thing was going to hold you.
        You have got to be kidding''')

    elif answer == '2':

        # The rope bridge looks flimsy... results = move forward

        deeper_desert()
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over("Some people just can't take the pressure...")


# FIRST (and only) step (ocean journey) in the blue door/ocean pathway

def ocean():
    print('\nYou have chosen the blue door')
    print('\nAll other doors disappear as you reach out for the door handle')
    print('After opening the door you are plunged into the deep, dark ocean')
    print('Which do you choose? (1, 2 or 0)')
    print('1). Swim for it and hope for the best')
    print('2). Dive down and see what is below')
    print("0). I can't swim")

    # User input to transition to the next stage

    answer = input('>')
    while answer not in ['1', '2', '0']:
        print('invalid key message')
        answer = input('>')
    if answer == '1':

        # Swim for it and hope for the best result = Game Over

        game_over('Seriously, ocean in all directions where are you going')
    elif answer == '2':

        # Dive down to the depths below = Move onto the desert step four

        pond()
    else:
        answer == '0'

        # This will end the game & ask the User if they wish to start again

        game_over('Seriously, You really should get lessons.')


# Game_over function that prints the reason from the initiating step

def game_over(reason):
    print('\n' + reason)
    print('Game Over!')

    # asks the User if they wish to begin the game again

    play_again()


# Function which enables the user to restart the game

def play_again():
    print('\nDo you want to play again? (y or n)')
    answer = input('>').lower()
    if 'y' in answer:
        start()
    else:
        exit()


# The following function is the initial step of the journey

def dragon():
    print('\nAmazing, you actually made it.')
    print('\nYou now stand before the Dragon')
    print('\nAsk you question and receive infinate wisdom:')
    print('\nBut beware, you only get three chances')
    i = 1
    while i < 4:

        # User input to transition to the next stage

        answer = input('What be thy question\n')
        print('Thinking...\n')
        time.sleep(random.randrange(0, 3))
        print(random.choice(dragon_talk))
        print('\nDo you have another question for the Dragon?')
        answer = input('>').lower()
        if 'y' in answer:
            i += 1
            continue
        else:
            game_over('Fair thee well, Oh mighty warrior!')
    else:

        # This will end the game & ask the User if they wish to start again

        game_over("Don't be so greedy. Begone with you!!!")


dragon_talk = [
    'If you Believe, then it will happen',
    'Live and let live',
    '42',
    'Is that really the question you wanted to ask',
    'Maybe, if you win the lottery',
    'Highly unikely',
    'It is a possibility, in the distant future',
    'If you are at one with the force',
    'The stars are aligned, so it must be so',
    'Life is short, go for it',
    'Hard No!',
    'You really need to chill out',
    'Are you speaking English? I thought not',
    'Maybe you should talk to someone else',
    "Don't count on it",
    'Unlikely at this time',
    'My sources say do not even try it',
    'Go hug your teddy bear',
    'Very Doubtful',
    ]

# start the game

start()
