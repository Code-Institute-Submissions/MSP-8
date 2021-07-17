import random
import time
from termcolor import cprint

# begining of the game, obtaining Users Name for a personalised experience

def begin():
    print("          )\         O_._._._A_._._._O         /(0              ")
    print("           \`--.___,'=================`.___,--'/                ")
    print("            \`--._.__                 __._,--'/                 ")
    print("              \  ,. l`~~~~~~~~~~~~~~~'l ,.  /                   ")
    print("  __            \||(_)!_!_!_.-._!_!_!(_)||/            __       ")
    print("  \\`-.__        ||_|____!!_|;|_!!____|_||        __,-'//       ")
    print("   \\    `==---='-----------'='-----------`=---=='    //        ")
    print("   | `--.                                         ,--' |        ")
    print("    \  ,.`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /         ")
    print("      \||  ____,-------._,-------._,-------.____  ||/           ")
    print("       ||\|___!`======='!`======='!`======='!___|/||            ")
    print("       || |---||--------||-| | |-!!--------||---| ||            ")
    print("_____O_ll_lO_____O_____O|| |'|'| ||O_____O_____Ol_ll_O_____O__  ")
    print("H o o H o o H o o H o o |-----------| o o H o o H o o H o o H o ")
    print("H_____H_____H_____H____O =========== O____H_____H_____H_____H___")
    print("                     /|=============|\                          ")
    print("___()______()______() '==== +-+ ====' ()______()______()______()")
    print("{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||")
    print("   ||      ||     / |==== s(   )s ====| \     ||      ||      ||")
    print("=================()  =================  ()======================")
    print("-----------------/| ------------------- |\----------------------")
    print("                / |---------------------| \                     ")
    print("--'           ()  '---------------------'  ()                   ")
    print("              /| ------------------------- |\    --'--'--'      ")
    print("  --'--'     / |---------------------------| \    '--'          ")
    print("           ()  |___________________________|  ()           '--'-")
    print("-          /| _______________________________  |\               ")
    print("          / |__________________________________| \              ")
    print("Welcome Truth Seeker")
    time.sleep(random.randrange(0, 2))
    name = input("By what name are you known?:\n").capitalize()
    time.sleep(random.randrange(0, 2))
    print(f"Welcome Mighty {name}!")
    start(name)

# The following function is the initial step of the journey

def start(name):
    print('\nYou seek the wisdom of the Dragon to answer your questions?')
    print('\nThe journey is long and arguous, but rewarding!\n')
    time.sleep(random.randrange(2, 4))
    cprint('''         _____________________________________________
        |.'',                                     ,''.|
        |.'.'',                                 ,''.'.|
        |.'.'.'',                             ,''.'.'.|
        |.'.'.'.'',                         ,''.'.'.'.|
        |.'.'.'.'.|                         |.'.'.'.'.|
        |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
        |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
        |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
        |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
        |,',',',',|---|',|'|???????|'|,'|---|,',',',',|
        |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
        |.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
        |.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
        |.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
        |.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
        |.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
        |.'.','         /%%%%%%%%%%%%%\         ','.'.|
        |.','          /%%%%%%%%%%%%%%%\          ','.|
        |;____________/%%%%%%%%%%%%%%%%%\____________;| ''')
    print('\nTo begin, you walk down a long, dark corridor')
    print('At the end you are faced with three doors')
    time.sleep(random.randrange(0, 2))
    print('Which do you choose? (1, 2 or 3)\n')
    cprint("   _____   ", 'yellow')
    cprint("  /_____\  ", 'yellow')
    cprint("  |  |  |      1) Bright Yellow door", 'yellow')
    cprint("  |  |  |          to the left", 'yellow')
    cprint(" @|__|__|@ ", 'yellow')
    cprint(" --=====-- \n", 'yellow')
    cprint("   _____   ", 'green')
    cprint("  /_____\  ", 'green')
    cprint("  |  |  |      2) Deep Green door", 'green')
    cprint("  |  |  |          directly ahead", 'green')
    cprint(" @|__|__|@ ", 'green')
    cprint(" --=====-- \n", 'green')
    cprint("   _____   ", 'blue')
    cprint("  /_____\  ", 'blue')
    cprint("  |  |  |      2) Pale Blue door", 'blue')
    cprint("  |  |  |          to the right", 'blue')
    cprint(" @|__|__|@ ", 'blue')
    cprint(" --=====-- ", 'blue')
    print('\n0). Runaway while you can coward......')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')

    # Validation and display surrounding invlaid character

    while answer not in ['1', '2', '3', '0']:
        time.sleep(random.randrange(0, 2))
        cprint("  _   _   _   _   _   _   _   _   _   _  ", 'red')
        cprint("_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_", 'red')
        cprint("-| |-| |-| |-| |-| |-| |-| |-| |-| |-| |-", 'red')
        cprint(" | | | | | | | | | | | | | | | | | | | | ", 'red')
        cprint("_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_", 'red')
        cprint("-| |-| |-| |-| |-| |-| |-| |-| |-| |-| |-", 'red')
        cprint(" |_| |_| |_| |_| |_| |_| |_|||_| |_| |_| ", 'red')
        cprint(",,,,,,||,,,,,,,,,,,,,,,,,,,,||,,,,,,,,,,,", 'red')
        print(f'Ah here {name}, You just run into the wall,')
        print('How about you try using a door...')
        answer = input('>')

    # lead the User into the desert adventure pathway

    if answer == '1':
        time.sleep(random.randrange(0, 2))
        desert()

    # lead the User into the forest adventure pathway
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        forest()

    # lead the User into the ocean/water adventure pathway
    elif answer == '3':
        time.sleep(random.randrange(0, 2))
        ocean()

    # This will end the game & ask the User if they wish to start again
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        game_quit('Then what are you doing here... get lost!!!')


# FIRST step (desert journey) in the yellow door/desert pathway

def desert():
    cprint('\nYou have chosen the yellow door', 'yellow')
    cprint('All other doors disappear as you choose', 'yellow')
    time.sleep(random.randrange(0, 2))
    cprint('''As soon as the door opens, you are hit by a blast of heat.\n
              \  :  /
               ' _ '
           -= ( (_) ) =-
               .   .
              /  :  \ 
          .-.    '
          |.|
        /)|`|(\ 
       (.(|'|)`)
    ~~~~`\`'./'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          |.|           ~~
          |`|                            ~~
         ,|`|.      (_)          ~~
          ```        \"\ 
               ~~     ^~^                    ''', 'yellow')
    cprint('''You are in the middle of the desert''', 'yellow')
    time.sleep(random.randrange(0, 2))
    cprint('\nWhere do you go from here? (1, 2 or 0)')
    cprint('1). Head straight into the dunes')
    cprint('2). Turn right and hope to find an end to this heat')
    cprint("0). Nah, I'm out, I need Air conditioning")

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')

    #handles invalid input
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('\nI know you are hot and tired, but you need to make a choice')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Head straight into the dunes result =head further

        deeper_desert()
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Turn right and hope to find an end to this heat

        game_over('''There is no end to this heat.
        You end up lost in the expanse of sand,
        looks like you won't be seeing the Dragon today.''')
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("Leaving so soon... Fine chicken out why don't you...")


# SECOND step (deeper into desert journey) in the yellow door/desert pathway

def deeper_desert():
    print('\nIn front of you stretches desert for miles and miles', 'yellow')
    print('After stumbling forward for what feels like eternity,', 'yellow')
    print('you think you see an oasis off in the distance', 'yellow')
    cprint('''                         \       /            _\/_
                             .-'-.              //o\  _\/_
          _  ___  __  _ --_ /     \ _--_ __  __ _ | __/o\\ _
        =-=-_=-=-_=-=_=-_= -=======- = =-=_=-=_,-'|"'""-|-,_ 
         =- _=-=-_=- _=-= _--=====- _=-=_-_,-"          |
           =- =- =-= =- = -  -===- -= - ." ''', 'yellow')
    time.sleep(random.randrange(0, 2))
    print('\nDo you: (1, 2 or 0)')
    print('1). Run towards the oasis and hope that it is real')
    print('2). Convince yourself that you are hallucinating and keep going')
    print('0). Run away')

    # Accept user input,allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('''I know you are hot and sweaty,
        but moving forward if the only way to go!''')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Turn towards the oasis and hope that it is real result =move forward

        oasis()
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Convince yourself... = Game Over

        game_over('''What are you, Crazy?
        Like for real, who would choose the desert over an oasis!''')
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("Oooooo, Look who can't take the heat......")


# THIRD step (oasis step the desert journey) in the yellow door/desert pathway

def oasis():
    print('\nUpon Reaching the oasis you find relief', 'yellow')
    print('in the shade of the tree branches', 'yellow')
    cprint('''                ___   ____
                /' --;^/ ,-_\     \ | /
               / / --o\ o-\ \\   --(_)--
              /-/-/|o|-|\-\\|\\   / | \
               '`  ` |-|   `` '
                     |-|
                     |-|O
                     |-(\,__
                  ...|-|\--,\_....
              ,;;;;;;;;;;;;;;;;;;;;;;;;,.
        ~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
        ~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,''', 'yellow')
    print('A short way into the oasis you see a small pond', 'yellow')
    print('\nDo you: (1, 2 or 0)')
    print('1). Have a drink before continuing into the desert')
    print('2). Dive in and enjoy a swim in the cool water')
    print('0). Run away')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('What? Did you fall asleep under a tree? Make a choice already')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Have a drink before continuing into the desert result = Game Over

        game_over('''Did you hit your head or something,
        why would you choose the desert over a swim''')
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Dive in and enjoy a swim in the cool water result = move forward

        pond()
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("Ooooo, Look who can't take the heat.....")


# FOURTH step (deeper into desert journey) in the yellow door/desert pathway

def pond():
    time.sleep(random.randrange(0, 2))
    cprint('''      
           .-;``  ``-.
          /   \       `\_..
          |-"``;-.      || `\ 
           \    `.`-.   /|  /
            `-.   `. \  |-``
               `-.  ) \ |
                /` /  / |
               / /`   | |
              / (     ) /
            _(   `-,-`_/
           /  `""""";`
           `---..---`
              //\\
             //---0
           _//_____
                   `\ 
                    (~^~_-~^-~^_~^~^-~^_ ''', 'blue')
    print('\nWhile swimming you notice a cave within the shallows', 'blue')
    time.sleep(random.randrange(0, 2))
    print('\nDo you: (1, 2 or 0)')
    print('1). Take a deep breath and dive into the unknown')
    print('2). Keep swimming and forget about the cave')
    print('0). Run away')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print("This isn't like the beer advert,")
        print("there is no wildcard 'Option C'")
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Take a deep breath and dive into the unknown result = move forward

        dragon()
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Keep swimming and forget about the cave result = Game Over

        game_over('''The Cave is just way too much adventure for you,
        Instead you abandon your quest and live out your days in the oasis''')
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit('So close and yet so far......')


# FIRST step (forest journey) in the green door/forest pathway

def forest():
    cprint('\nYou have chosen the green door', 'green')
    cprint('All other doors disappear as you choose', 'green')
    cprint('After opening the door you find yourself', 'green')
    cprint('''      /\             /\             /\      
     /\*\           /\*\           /\*\     
    /\O\*\         /\O\*\         /\O\*\    
   /*/\/\/\       /*/\/\/\       /*/\/\/\   
  /\O\/\*\/\     /\O\/\*\/\     /\O\/\*\/\  
 /\*\/\*\/\/\   /\*\/\*\/\/\   /\*\/\*\/\/\ 
/\O\/\/*/\/O/\ /\O\/\/*/\/O/\ /\O\/\/*/\/O/\ 
      ||             ||             ||      
      ||             ||             ||      
      ||             ||             ||''', 'green')
    cprint('in the middle of a tropical forest', 'green')
    print('\nWhich do you choose? (1, 2 or 0)')
    print('1). Try to forge a path forward deeper into the undergrowth')
    print('2). Climb the biggest tree you can find, for a better view')
    print('0). Ew, mosquitoes')

# Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('There is no going back now, make a choice, forward or up.')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Try to forge a path forward... = move forward

        deeper_forest()
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Climb the biggest tree you can find... = Game Over

        game_over('''The view from the top of the tree is amazing.
        Forest as far as the eye can see.
        Too bad the branch broke and you fell to the ground''')
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("Leaving so soon... Fine chicken out why don't you...")


# SECOND step (finding the gorge) in the green door/forest pathway

def deeper_forest():
    print('\nYou forge a path forward throw the thick undergrowth', 'green')
    print('Eventually you reach a large gorge', 'green')
    cprint('''
           _________....-~    ~-.______
        ~~~                            ~~~~-----...___________..--------
                                                   |   |     |
                                                   | |   |  ||
                                                   |  |  |   |
                                                   |'. .' .`.|
        ___________________________________________|0oOO0oO0o|____________
         -          -         -       -      -    / '  '. ` ` \    -    -
              --                  --       --   /    '  . `   ` \    --
        ---            ---          ---       /  '                \ ---
             ----               ----        /       ' ' .    ` `    \  ----
        -----         -----         ----- /   '   '        `      `   \ 
             .-~~-.          ------     /          '    . `     `    `  \ 
        ''', 'green')
    print('You notice some vines that hang across the gap', 'green')
    print('\nDo you? (1, 2 or 0)')
    print('1). Swing across like Tarzan')
    print('2). Walk along the edge to find a safer way across')
    print('0). Nope, Heights are just way to much')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('Seriously dude, make a choice')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Swing across like Tarzan result = Game Over

        game_over('''What the frell. This is not a movie.
        How could you possibly think you could swing on a vine''')
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Walk along the edge to find a safer way across = Move Forward

        gorge()
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("So I guess you don't need the Dragon's answers")


# THIRD step (crossing the gorge) in the green door/forest pathway

def gorge():
    print('\nYou walk along the edge until the sun is low in the sky', 'green')
    print('Just as you are about to give up you see a rope bridge ahead', 'green')
    cprint('''                             ___....___
                     __..-:'':__:..:__:'':-..__
                 _.-:__:.-:'':  :  :  :'':-.:__:-._
               .':.-:  :  :  :  :  :  :  :  :  :._:'.
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
  !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]
           [ ]                                        [ ]
     jgs   [ ]                                        [ ]
   ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^ ''', 'green')
    print('\nDo you? (1, 2 or 0)')
    print('1). Carefully, but quickly, cross the rope bridge')
    print('2). The rope bridge looks flimsy,')
    print('    cotinue along the edge of the gorge')
    print('0). Got a problem with heights do ya princess?')

    # Accept user input, allowing choices, option to quit and invalid function

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('Are you trying to fall off the edge, pick a direction.')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Carefully, but quickly, cross the rope bridge result = Game Over

        game_over('''You seriously thought this old thing was going to hold you.
        You have got to be kidding''')

    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # The rope bridge looks flimsy... results = move forward

        deeper_desert()
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit("Some people just can't take the pressure...")


# FIRST (and only) step (ocean journey) in the blue door/ocean pathway

def ocean():
    print('\nYou have chosen the blue door', 'blue')
    print('All other doors disappear as you choose', 'blue')
    time.sleep(random.randrange(0, 2))
    cprint('''                                  .-"""-.
                             /       \ 
                            ;_.-"""-._;
         .,_       __,.---.-(=(o)-(o)=)-.---.,__       _,.
         '._'--"```          \   ^   /          ```"--'_.'
            ``"''~---~~%^%^.%.`._0_.'%,^%^%^~~---~''"``
            ~^~- `^-% ^~.%~%.^~-%-~.%-^.% ~`% ~-`%^`-~^~
               ~^- ~^- `~.^- %`~.%~-'%~^- %~^- ~^ ''')
    print('You are plunged into the deep, dark ocean', 'blue')
    time.sleep(random.randrange(0, 2))
    print('\nWhich do you choose? (1, 2 or 0)')
    print('1). Swim for it and hope for the best')
    print('2). Dive down and see what is below')
    print("0). I can't swim")

    # User input to transition to the next stage

    answer = input('>')
    while answer not in ['1', '2', '0']:
        time.sleep(random.randrange(0, 2))
        print('You will get tired if you stay where you are!')
        answer = input('>')
    if answer == '1':
        time.sleep(random.randrange(0, 2))
        # Swim for it and hope for the best result = Game Over

        game_over('Seriously, ocean in all directions where are you going')
    elif answer == '2':
        time.sleep(random.randrange(0, 2))
        # Dive down to the depths below = Move onto the desert step four

        pond()
    else:
        answer == '0'
        time.sleep(random.randrange(0, 2))
        # This will end the game & ask the User if they wish to start again

        game_quit('Seriously, You really should get lessons.')


# Game_over function that prints the reason from the initiating step

def game_over(reason):
    time.sleep(random.randrange(0, 3))
    print('\n' + reason)
    print('Game Over!')
    print("             ___        ")
    print("            /   \\      ")
    print("       /\\ | . . \\     ")
    print("     ////\\|     ||     ")
    print("   ////   \\ ___//\     ")
    print("  ///      \\      \    ")
    print(" ///       |\\      |   ")
    print("//         | \\  \   \  ")
    print("/          |  \\  \   \ ")
    print("           |   \\ /   / ")
    print("           |    \/   /  ")
    print("           |     \\/|   ")
    print("           |      \\|   ")
    print("           |       \\   ")
    print("           |        |   ")
    print("           |_________\  ")

    # asks the User if they wish to begin the game again

    play_again()


def game_quit(reasonquit):
    time.sleep(random.randrange(0, 3))
    print('\n' + reasonquit)
    print('Game Over!')
    cprint(''' 
     _______________
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .------.
      .`  * * *  `.
     :  *       *  :
    : ~  QUITTER  ~ :
     :  *       *  :
      `.  * * *  .'
        `-.....-` ''', 'red')

    # asks the User if they wish to begin the game again

    play_again()

# game over message for once the game is complete
def game_complete(reason):
    time.sleep(random.randrange(0, 3))
    print('\n' + reason)
    cprint('''                       /\ 
                _/\           /  \ 
            _  /   \         /    \/\ 
           / \/   _ \     /\/\  _  _/\ 
          /   \_ / \/\_/\/_/  \/ \/   \ 
         /\/\   \_   /   \/            \ 
        /    \___/\ /     \             \ 
                   \       \             \ 
                   .-"---.  \             \ 
        __..---.. /       \  \             \ 
                 /\___.-'./\''--..____..--''
        `-.      \/ O) (O \/ ''--.._
            __    |  (_)  |         _.-'-._
           / /  __/\\___//\__ ..--''-._
           | (_/\ \/`---'\/ /\         `-._
        _.-\ \/  \  \   /  /  \.-'-._
           /\|   /  -| |-  \   \     `-._
          | ||  /\  -| |-  /\   \        `-.
           \/|_/ |  -|_\-  |/   /
           \ \   /  /B_B\  \\  /
           / (   \_/  _  \_/ \/
        .__\ \   /    |    \_/
           ) /''-| __ | __ |
           |(    \    |    /---...___
       /|    /____|____\         '-._
           ||     |   ||   |
           \\     ///\\//\\\ 
            \|   oOO(_)(_)OOo''')
    print('Game Over!')

    # asks the User if they wish to begin the game again

    play_again()

# Function which enables the user to restart the game

def play_again():
    time.sleep(random.randrange(0, 3))
    print('\nDo you want to play again?')
    answer = input('>').lower()
    if 'y' in answer:
        begin()
    else:
        exit()


# The following function is the initial step of the journey

def dragon():
    print('\nAmazing, you actually made it.', 'magenta')
    time.sleep(random.randrange(0, 3))
    cprint('''                 ___====-_  _-====___
                   _--^^^#####//      \\#####^^^--_
                _-^##########// (    ) \\##########^-_
               -############//  |\^^/|  \\############-
             _/############//   (@::@)   \\############\_
            /#############((     \\//     ))#############\
           -###############\\    (oo)    //###############-
          -#################\\  / VV \  //#################-
         -###################\\/      \//###################-
        _#/|##########/\######(   /\   )######/\##########|\#_
        |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
        `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
           `   `  `      `   / | |  | | \   '      '  '   '
                            (  | |  | |  )
                           __\ | |  | | /__
                          (vvv(VVV)(VVV)vvv)''',  'magenta')
    time.sleep(random.randrange(0, 3))
    print('\nAsk you question and receive infinate wisdom:')
    print('\nBut beware, you can only ask THREE!!!\n')
    i = 1
    while i < 4:

        # User input to transition to the next stage

        answer = input('What be thy question?\n')
        print('Thinking...\n')
        time.sleep(random.randrange(0, 3))
        print(random.choice(dragon_talk))
        print('\nDo you have another question for the Dragon? (y or n)')
        answer = input('>').lower()
        if 'y' in answer:
            i += 1
            continue
        else:
            game_complete('Fair thee well, Oh mighty warrior!')
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

begin()
