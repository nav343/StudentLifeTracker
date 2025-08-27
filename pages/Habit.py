import pickle
import time
from utils.colors import COLORS
from utils.window import Window


def validateNature(window: Window) -> str:
    nature = window.input("Positive or Negative (+/-): ", color=COLORS.YELLOW)
    if nature == "+" or nature == "-":
        return nature
    else:
        window.print("Invalid Input. Expected + or -", color=COLORS.RED)
        return validateNature(window)


def CreateHabit(window: Window):
    window.rerender()
    title = window.input("Title: ", hidden=False, color=COLORS.LIGHT_GREEN)
    nature = validateNature(window)
    window.rerender()
    window.print(f"Title: {title}", color=COLORS.LIGHT_GREEN)
    if nature == "+":
        window.print("Positive or Negative (+/-): +", color=COLORS.LIGHT_GREEN)
    else:
        window.print("Positive or Negative (+/-): -", color=COLORS.LIGHT_RED)

    desc = window.input("Short Description: ", color=COLORS.YELLOW)
    file = open(".exoro_data/habit.dat", "wb+")
    pickle.dump({"title": title, "nature": nature, "desc": desc}, file)
    window.print("Created!!", color=COLORS.LIGHT_GREEN)
    time.sleep(0.5)


def getHabits() -> list:
    habits = []
    try:
        with open(".exoro_data/habit.dat", "rb+") as file:
            try:
                while True:
                    habits.append(pickle.load(file))
            except EOFError:
                return habits
    except FileNotFoundError:
        return []


def RemoveHabit(window: Window):
    window.print("WIP")


def Habit(window: Window) -> None:
    while True:
        window.rerender()
        window.print("HABIT TRACKER", color=COLORS.YELLOW, centered=True)
        habits = getHabits()
        if len(habits) == 0:
            window.print("You don't have any Habits!!", color=COLORS.LIGHT_BLUE)
            choice = int(
                window.input("Create one now?\n1. Yes\n2. No", color=COLORS.YELLOW)
            )
            if choice == 1:
                CreateHabit(window)
            else:
                window.rerender()
                break
        else:
            for habit in habits:
                window.print(str(habit), color=COLORS.GREEN)
            choice = int(
                window.input(
                    "What do you want to do?\n1. Add a habit\n2. Remove habit\n3. Go back"
                )
            )
            if choice == 1:
                CreateHabit(window)
            elif choice == 2:
                RemoveHabit(window)
            else:
                break
