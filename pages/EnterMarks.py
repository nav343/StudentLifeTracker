import pickle
import time

from utils.colors import COLORS
from utils.window import Window


def EnterMarks(window: Window) -> None:
    def validate(score, total) -> float:
        if score > total:
            window.print(
                "You lied. You cannot score more than the max marks.\n",
                color=COLORS.RED,
            )
            score = float(
                window.input(">>> How much did you score? (F): ", hidden=False)
            )
            return validate(score, total)
        else:
            return score

    window.rerender()
    window.print("Enter Marks ", centered=True, color=COLORS.LIGHT_BLUE)
    try:
        sub = window.input(">>> What subject (S): ", hidden=False)
        total = float(
            window.input(">>> What was the maximum score? (F): ", hidden=False)
        )
        score = float(window.input(">>> How much did you score? (F): ", hidden=False))

        score = validate(score, total)

        resultFile = open("./tests/result.dat", "ab+")
        data = {
            "sub": sub,
            "total": total,
            "score": score,
            "perc": (score / total) * 100,
        }
        pickle.dump(data, resultFile)
        window.print(
            "\nData entered successfully.\nRedirecting...", color=COLORS.LIGHT_GREEN
        )
        time.sleep(1)
        window.rerender()

    except Exception as E:
        window.print(str(E))
        window.quit()
