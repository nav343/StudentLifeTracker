import os
import pickle
import time
from utils.colors import COLORS
from utils.window import Window


def searchNotes() -> list:
    files = []
    for file in os.listdir("./tests/"):
        if file[0:4] == "Note" and file[-1:-4:-1][::-1] == "dat":
            files.append(file[5:-4])
    return files


def readNotes(window: Window) -> int:
    try:
        window.print("Your Todos", color=COLORS.YELLOW, centered=True)
        files = searchNotes()
        counter = 0
        if len(files) != 0:
            for i in files:
                window.print(f"{counter + 1}. {str(i)}", color=COLORS.LIGHT_GREEN)
                counter += 1
            window.print()
        else:
            window.print("You don't have any Notes", color=COLORS.LIGHT_BLUE)
            window.print("Redirecting...", color=COLORS.LIGHT_RED)
            time.sleep(2)

    except Exception as E:
        window.print("An unexpected error occurred. Please try again")
        window.print(str(E))
        exit()

    return counter


def createNotes(window: Window):
    title = window.input("Title: ", hidden=False, color=COLORS.LIGHT_BLUE)
    window.print("Creating...", color=COLORS.YELLOW)
    time.sleep(0.5)
    window.rerender()
    txt = window.editor("Notes")
    try:
        data = {
            "file": f"tests/Note_{str(title).replace(' ', '_')}.dat",
            "content": txt,
        }
        file = open(data["file"], "wb+")
        pickle.dump(data, file)
        file.close()
    except Exception:
        window.print("An unexpected error occurred. Try again", color=COLORS.RED)
        time.sleep(1)
    window.rerender()


def Notes(window: Window) -> None:
    while True:
        window.rerender()
        act = int(
            window.input(
                "Entering Notes mode....\n\n1. Read existing Notes\n2. Create new Note\n3. Go back",
                color=COLORS.YELLOW,
            )
        )

        match act:
            case 1:
                window.rerender()
                numberOfNotes = readNotes(window)
                if numberOfNotes != 0:
                    choice = ""
                    while True:
                        try:
                            choice = int(
                                window.input(
                                    "Which Note do you want to open?",
                                    color=COLORS.GREEN,
                                )
                            )
                            if choice > numberOfNotes:
                                window.print(
                                    f"Invalid index. You only have {numberOfNotes} notes.",
                                    color=COLORS.RED,
                                )
                            else:
                                break
                        except ValueError:
                            window.print("Invalid. Try again", color=COLORS.RED)

                    try:
                        noteFile = open(
                            f"tests/Note_{searchNotes()[choice - 1]}.dat", "rb"
                        )
                        data = pickle.load(noteFile)["content"]
                        window.rerender()
                        window.print(searchNotes()[choice - 1], color=COLORS.LIGHT_BLUE)
                        window.print("-" * (len(searchNotes()[choice - 1])))
                        window.print()
                        window.print(data)
                        window.print()
                        window.input(
                            "Press any key to go back.", color=COLORS.LIGHT_RED
                        )
                    except Exception as E:
                        window.print(str(E))
                        time.sleep(2)
            case 2:
                window.rerender()
                createNotes(window)
            case 3:
                window.rerender()
                break
            case _:
                window.print("Invalid", color=COLORS.RED)
                time.sleep(2)
