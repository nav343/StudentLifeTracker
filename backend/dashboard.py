# from operator import itemgetter

import datetime
from tabulate import tabulate
from pages.Habit import Habit
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

    name = userData["name"]

    window.print("Student Dashboard \n", centered=True, color=COLORS.LIGHT_BLUE)
    window.print(
        "/".join(str(datetime.datetime.now().date()).split("-")[::-1]),
        color=COLORS.LIGHT_RED,
        rightAlign=True,
    )
    window.print(f">> Welcome {name}.\n", color=COLORS.LIGHT_GREEN)
    options_cbse = [
        ["1. Enter marks", "2. View Past Result", "3. Open ToDo"],
        ["4. Open Textbook", "5. Open Notes", "6. Habit"],
        ["", "7. Exit", ""],
    ]
    while True:
        try:
            window.print("What do you want to do today?\n", color=COLORS.YELLOW)
            window.print(
                tabulate(
                    options_cbse,
                    tablefmt="fancy_grid",
                    stralign="center",
                    missingval="---",
                ),
                color=COLORS.LIGHT_GREEN,
            )
            action = int(window.input(""))
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
                    Habit(window)
                case 7:
                    window.print(">>> Thanks", color=COLORS.GREEN)
                    window.quit()
                case _:
                    window.rerender()
                    window.print("Invalid. Try again\n", color=COLORS.RED)
        except Exception:
            window.print("Invalid. Try again.\n", color=COLORS.RED)
