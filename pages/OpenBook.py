from utils.colors import COLORS
from utils.window import Window


def OpenBook(window: Window, userData: dict) -> None:
    _12 = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: "",
        13: "",
        14: "",
        15: "",
        16: "",
        17: "",
        18: "",
        19: "",
        21: "",
        20: "",
        22: "",
    }
    _12 = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: "",
        13: "",
        14: "",
        15: "",
        16: "",
        17: "",
        18: "",
        19: "",
        21: "",
        20: "",
        22: "",
    }

    _6to8 = {}
    _9 = {}
    _10 = {}

    while True:
        window.rerender()
        window.print(
            f"Open Textbook for class {userData['board']} {userData['std']}",
            color=COLORS.YELLOW,
        )
        if int(userData["std"]) <= 5:
            window.print("WIP 1 to 5")
        elif int(userData["std"]) <= 8 and int(userData["std"]) >= 6:
            window.print("WIP 6 to 8")
        elif int(userData["std"]) == 9:
            window.print("WIP 9")
        elif int(userData["std"]) == 10:
            window.print("WIP 10")
        elif int(userData["std"]) == 11:
            window.print("WIP 11")
        elif int(userData["std"]) == 12:
            window.print("WIP 12")

        else:
            window.print(
                "Sorry!!. Books for your class are not available.", color=COLORS.RED
            )

        window.input("Press any key to go back...", color=COLORS.LIGHT_RED)
        window.rerender()
        break
