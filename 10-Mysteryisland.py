print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
""")
while True:
    door = input("""
Welcome to my island!
There are two doors in front of you. 🚪 a red door and 🚪 a blue door
Which door do you want to open?
    """)

    if door.lower() == "blue":
        print("Oops! You chose the crocodile door.\nGame over!")
    elif door.lower() == "red":
        box = input("""
Great! now you entered a room.
you found three boxes: 🎁 white, 🎁 black, 🎁 green
Which box do you open?
        """)
        if box.lower() == "white":
            print("Oops! You opened a box filled with snakes 🐍🐍🐍")
        elif box.lower() == "black":
            print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️")
        elif box.lower() == "green":
            print("Congratulations! You found the treasure! 💰 💰 💰 ")
            break
        else:
            print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
    else:
        print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")