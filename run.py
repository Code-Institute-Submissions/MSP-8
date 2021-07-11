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
