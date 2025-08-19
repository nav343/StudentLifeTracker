# from operator import itemgetter

import datetime
from pages.Notes import Notes
from pages.OpenBook import OpenBook
from pages.PastResult import PastResult
from pages.EnterMarks import EnterMarks
from pages.Todo import Todo
from utils.colors import COLORS
from utils.window import Window
from utils.loader import Loader

logo = """
███████╗██╗░░██╗░█████╗░██████╗░░█████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░░╚███╔╝░██║░░██║██████╔╝██║░░██║
██╔══╝░░░██╔██╗░██║░░██║██╔══██╗██║░░██║
███████╗██╔╝╚██╗╚█████╔╝██║░░██║╚█████╔╝
╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░
"""


def Dashboard(window: Window, userData: dict, redirected: bool = False):
    if not redirected:
        Loader(window, logo, speed=0.1)

    """
    name, age, std, subs, favsub, prevperc = itemgetter(
        "name", "age", "std", "subs", "favsub", "prevperc"
    )(userData)
    """
    name = userData["name"]
    board = userData["board"]

    window.print("Student Dashboard \n", centered=True, color=COLORS.LIGHT_BLUE)
    window.print(
        "/".join(str(datetime.datetime.now().date()).split("-")[::-1]),
        color=COLORS.LIGHT_RED,
        rightAlign=True,
    )
    window.print(f">> Welcome {name}.\n", color=COLORS.LIGHT_GREEN)
    options_cbse = [
        "Enter marks",
        "View Past Result",
        "Open ToDo",
        "Open Textbook",
        "Open Notes",
        "Exit",
    ]
    options_oth = [
        "Enter marks",
        "View Past Result",
        "Open ToDo",
        "Open Notes",
        "Exit",
    ]
    while True:
        try:
            """
            action = int(
                window.input(
                    f"What do you want to do today?\n1. Enter marks\n2. View past result\n3. Open Todos\n{'4. Open Textbook\n' if str(board).lower() == 'cbse' else ''}{'5' if str(board).lower() == 'cbse' else '4'}. Notes\n{'6' if str(board).lower() == 'cbse' else '5'}. Quit",
                    color=COLORS.YELLOW,
                )
            )
            """
            window.print("What do you want to do today?", color=COLORS.YELLOW)
            action = (
                window.menu(
                    options_cbse if str(board).lower() == "cbse" else options_oth,
                    color=COLORS.YELLOW,
                )
                + 1
            )
            if str(board).lower() == "cbse":
                match action:
                    case 1:
                        EnterMarks(window)
                    case 2:
                        PastResult(window)
                    case 3:
                        Todo(window)
                    case 4:
                        OpenBook(window, userData)
                    case 5:
                        Notes(window)
                    case 6:
                        window.print(">>> Thanks", color=COLORS.GREEN)
                        window.quit()
                    case _:
                        window.rerender()
                        window.print("Invalid. Try again\n", color=COLORS.RED)
            else:
                match action:
                    case 1:
                        EnterMarks(window)
                    case 2:
                        PastResult(window)
                    case 3:
                        Todo(window)
                    case 4:
                        Notes(window)
                    case 5:
                        window.print(">>> Thanks", color=COLORS.GREEN)
                        window.quit()
                    case _:
                        window.rerender()

        except Exception:
            window.print("Invalid. Try again.\n", color=COLORS.RED)
