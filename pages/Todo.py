import time
import pickle

from utils.colors import COLORS
from utils.window import Window

"""
# OLD ALGO

def createTodo(window: Window) -> None:
    txt = window.editor("Todo Editor ")
    data = {
        "file": f".exoro_data/TODO_{datetime.datetime.now().date()}-{datetime.datetime.now().time()}.dat",
        "data": txt,
    }
    file = open(data["file"], "wb+")
    pickle.dump(data, file)
    file.close()


def searchTodo() -> dict:
    files = {}
    for file in os.listdir(".exoro_data/"):
        if file[0:4] == "TODO":
            dateFormat = f"{file[13:15]}/{file[10:12]}/{file[5:9]} ({file[16:18]})HR ({file[19:21]})MIN"
            spoilerFile = open(".exoro_data/" + file, "rb")
            data = str(pickle.load(spoilerFile)["data"])
            spoiler = data[0 : (30 if len(data) >= 30 else len(data))] + "..."
            spoilerFile.close()
            files[dateFormat] = spoiler
    return files


def readTodo(window: Window) -> int:
    try:
        window.print("Your Todos", color=COLORS.YELLOW, centered=True)
        files = searchTodo()
        if len(files) != 0:
            counter = 1
            for i in files:
                window.print(
                    f"{counter}. {str(i)} ---> {str(files[i]).replace('\n', ' ')}"
                )
                counter += 1
            window.print()
            return counter - 1
        else:
            window.print(
                "You don't have any Todos.\nCreate one now?", color=COLORS.LIGHT_BLUE
            )
            return 0

    except Exception as E:
        window.print("An unexpected error occurred. Please try again")
        window.print(str(E))
        exit()


    choice = window.input("Go back? (OR n to QUIT)", color=COLORS.LIGHT_GREEN)
    if choice == "n":
        window.quit()
"""


def searchTodo() -> tuple[int, list]:
    file = None
    try:
        file = open(".exoro_data/todo.dat", "rb")
    except FileNotFoundError:
        return (0, [])
    counter = 0
    data = []
    try:
        while True:
            data.append(pickle.load(file))
            counter += 1
    except EOFError:
        file.close()
        return (counter, data)


def updateTodo(newData):
    file = open(".exoro_data/todo.dat", "wb")
    for i in newData:
        pickle.dump(i, file)
    file.close()


def readTodo(window: Window) -> None:
    try:
        window.print("Your Todos", color=COLORS.YELLOW, centered=True)
        (count, data) = searchTodo()
        if count != 0:
            for i in range(count):
                window.print(
                    f"({'✓' if data[i]['checked'] else '○'}) ({i + 1}) -> {data[i]['data']}".strip()
                )
            window.print()

            completed = window.input(
                "Which TODO did you complete? (or q to go back)",
                color=COLORS.LIGHT_BLUE,
            )
            if str(completed).isdigit():
                if int(completed) - 1 <= len(data):
                    data[int(completed) - 1]["checked"] = (
                        True if not data[int(completed) - 1]["checked"] else False
                    )
                    updateTodo(data)
                else:
                    window.print(
                        f"Cannot access TODO {completed} as you only have {len(data)} TODO(s)",
                        color=COLORS.RED,
                    )
                    time.sleep(1)
        else:
            window.print(
                "You don't have any Todos.\nCreate one now?", color=COLORS.LIGHT_BLUE
            )
            window.input("")

    except Exception as E:
        window.print("An unexpected error occurred. Please try again")
        window.print(str(E))
        exit()


def createTodo(window: Window) -> None:
    txt = window.editor("Todo Editor ")
    file = open(".exoro_data/todo.dat", "ab+")
    pickle.dump({"data": txt, "checked": False}, file)
    file.close()


def Todo(window: Window) -> None:
    while True:
        window.rerender()
        act = int(
            window.input(
                "Entering Todo mode....\n\n1. Read existing Todo's\n2. Create new Todo\n3. Go back",
                color=COLORS.YELLOW,
            )
        )

        match act:
            case 1:
                window.rerender()
                readTodo(window)
            case 2:
                window.rerender()
                createTodo(window)
            case 3:
                window.rerender()
                break
            case _:
                window.print("Invalid", color=COLORS.RED)
                time.sleep(2)
