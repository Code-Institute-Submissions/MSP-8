# The following function is the initial step of the journey, the kick off screen
def start():
    print("\nSo, you seek the wisdom of the Dragon to answer your questions?")
    print("\nThe journey is long and arguous, but rewarding!")
    print("To begin, you walk down a long, dark corridor")
    print("At the end you are faced with three doors")
    print("Which do you choose? (1, 2 or 3)")
    print("1). Bright Yellow door to the left")
    print("2). Deep Green door directly ahead")
    print("3). Brilliant Blue door to the right")
    print("0). Runaway while you can coward......")

    # Accept user input, allowing choices, option to quit and invalid function
    answer = input(">")
    # Validation and display surrounding invlaid character
    while answer not in ["1", "2", "3", "0"]:
        print("Ah here, You just run into a door, how about you try using a door...")
        answer = input(">")
    if answer == "1":
        # lead the User into the desert adventure pathway
        desert()
    elif answer == "2":
        # lead the User into the forest adventure pathway
        forest()
    elif answer == "3":
        # lead the User into the ocean/water adventure pathway
        ocean()
    else:
        answer == "0"
        # This will end the game and ask the User if they wish to start again
        game_over("Then what are you doing here... get lost already")

###############################################################################################
# FIRST step (desert journey) in the yellow door/desert pathway
def desert():
    print("\nYou have chosen the yellow door")
    print("\nAll other doors disappear as you reach out for the door handle")
    print("As soon as the door opens, you are hit by a blast of heat.")
    print("You are in the middle of the desert.")
    print("Which do you choose? (1, 2 or 0)")
    print("1). Head straight into the dunes")
    print("2). Turn right and hope to find an end to this heat")
    print("0). Nah, I'm out, I need Air conditioning")

    # Accept user input, allowing choices, option to quit and invalid function
    answer = input(">")
    while answer not in ["1", "2", "0"]:
        print("I know you are hot and tired, but you need to make a choice")
        answer = input(">")
    if answer == "1":
        # Head straight into the dunes result = head further
        deeper_desert()
    elif answer == "2":
        # Turn right and hope to find an end to this heat = result Game Over
        game_over("There is no end to the Heat. You end up lost in the expanse of sand, looks like you won't be seeing the Dragon today.")
    else:
        answer == "0"
        # This will end the game and ask the User if they wish to start again
        game_over("Leaving so soon.......... Fine chicken out why don't you...")