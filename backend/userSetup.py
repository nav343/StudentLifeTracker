import pickle
from utils.loader import Loader
from utils.window import Window
from utils.colors import COLORS


logo = """
███████╗██╗░░██╗░█████╗░██████╗░░█████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░░╚███╔╝░██║░░██║██████╔╝██║░░██║
██╔══╝░░░██╔██╗░██║░░██║██╔══██╗██║░░██║
███████╗██╔╝╚██╗╚█████╔╝██║░░██║╚█████╔╝
╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░
"""


def CreateUser() -> dict:
    window = Window()
    Loader(window, logo, speed=0.1)
    window.print("Create Account\n", centered=True, color=COLORS.LIGHT_GREEN)
    window.print(
        "Hi there. \nGood to have you with us.\nSeems like you are new here. Let's quickly create a profile!!\n"
    )
    window.print("Instructions", color=COLORS.YELLOW)
    window.print(
        "Each value has to be correctly filled with the required type of answer."
    )
    window.print(
        "\nS -> Plain text (alphabets, numbers etc)\nI -> Integers\nF -> Decimal/Integer numbers",
        color=COLORS.LIGHT_GREEN,
    )
    reminder = window.input("Shall we proceed? (n to quit. Enter to continue)")
    if reminder.lower() == "n":
        window.quit()

    window.rerender()
    name = window.input(
        "What's your name? (S): ", hidden=False, color=COLORS.YELLOW
    ).title()
    age = int(window.input("What's your age? (I): ", hidden=False))
    std = int(window.input("What class are you studying in? (I): ", hidden=False))
    board = window.input(
        "What board is your school affiliated with? (S): ", hidden=False
    ).upper()
    subs = int(
        window.input(
            "How many subjects do you have in your school? (I): ", hidden=False
        )
    )
    favsub = window.input(
        "What's you favourite subject? (S): ", hidden=False, canBeEmpty=True
    )
    prevperc = float(
        window.input(
            f"How much did you score in your last class? ({std - 1}) (F): ",
            hidden=False,
        )
    )

    window.rerender()
    window.print("Confirm Details\n", color=COLORS.YELLOW)
    window.print(
        f"Name: {name}\nAge: {age}\nClass: {std}\nBoard: {board}\nNumber of Subjects: {subs}\nFavourite Subject: {favsub}\nPrevious class %age: {prevperc}\n\n"
    )
    confirm = window.input(
        "Are the details correct?\nShall we proceed? (y to continue, n to quit)"
    )
    if confirm.lower() == "n":
        window.quit()
    data = {
        "name": name,
        "age": age,
        "std": std,
        "subs": subs,
        "favsub": favsub,
        "prevperc": prevperc,
        "board": board,
    }
    setupFile = open("tests/user_data.dat", "wb+")
    pickle.dump(data, setupFile)
    setupFile.close()
    window.print("\n\nSetup successful.")

    return data
