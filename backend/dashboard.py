# from operator import itemgetter

import datetime
from pages.PastResult import PastResult
from pages.EnterMarks import EnterMarks
from pages.Todo import Todo
from utils.colors import COLORS
from utils.window import Window
from utils.loader import Loader


def Dashboard(window: Window, userData: dict, redirected: bool = False):
    if not redirected:
        Loader(window, "WELCOME ", speed=0.1)

    """
    name, age, std, subs, favsub, prevperc = itemgetter(
        "name", "age", "std", "subs", "favsub", "prevperc"
    )(userData)
    """
    name = userData["name"]

    window.print("Student Dashboard \n", centered=True, color=COLORS.LIGHT_BLUE)
    window.print(
        "/".join(str(datetime.datetime.now().date()).split("-")[::-1]),
        color=COLORS.LIGHT_RED,
        rightAlign=True,
    )
    window.print(f">> Welcome {name}.\n", color=COLORS.LIGHT_GREEN)
    while True:
        try:
            action = int(
                window.input(
                    "What do you want to do today?\n1. Enter marks\n2. View past result\n3. Open Todos\n4. Quit",
                    color=COLORS.YELLOW,
                )
            )
            match action:
                case 1:
                    EnterMarks(window)
                case 2:
                    PastResult(window)
                case 3:
                    Todo(window)
                case 4:
                    window.print(">>> Thanks", color=COLORS.GREEN)
                    window.quit()
                case _:
                    window.rerender()
                    window.print("Invalid. Try again\n", color=COLORS.RED)
        except Exception:
            window.print("Invalid. Try again.\n", color=COLORS.RED)
