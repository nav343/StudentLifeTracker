import datetime
import time
import os
import pickle

from utils.colors import COLORS
from utils.window import Window


def createTodo(window: Window) -> None:
    txt = window.editor("Todo Editor ")
    data = {
        "file": f"tests/{datetime.datetime.now().date()}-{datetime.datetime.now().time()}.dat",
        "data": txt,
    }
    file = open(data["file"], "wb+")
    pickle.dump(data, file)
    file.close()


def searchTodo() -> dict:
    files = {}
    reserved = ["user_data.dat", "result.dat"]
    for file in os.listdir("./tests/"):
        if file[-1:-4:-1][::-1] == "dat" and file not in reserved:
            dateFormat = f"{file[8:10]}/{file[5:7]}/{file[0:4]} ({file[11:13]})HR ({file[14:16]})MIN"
            spoilerFile = open("./tests/" + file, "rb")
            spoiler = str(pickle.load(spoilerFile)["data"][0:30] + "...")
            spoilerFile.close()
            files[dateFormat] = spoiler
    return files


def readTodo(window: Window) -> None:
    try:
        window.print("Your Todos", color=COLORS.YELLOW, centered=True)
        files = searchTodo()
        counter = 1
        for i in files:
            window.print(f"{counter}. {str(i)} ---> {str(files[i]).replace('\n', ' ')}")
            counter += 1
        window.print()

    except Exception as E:
        window.print("An unexpected error occurred. Please try again")
        window.print(str(E))
        exit()

    choice = window.input("Go back? (OR n to QUIT)", color=COLORS.LIGHT_GREEN)
    if choice == "n":
        window.quit()


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
