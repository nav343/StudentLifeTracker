import pickle
import time
from utils.colors import COLORS
from utils.window import Window


def PastResult(window: Window) -> None:
    window.rerender()
    window.print("Past Result ", color=COLORS.LIGHT_GREEN, centered=True)

    try:
        resultFile = open("./tests/result.dat", "rb")
        try:
            window.print()
            window.print(
                f"   Subject{' ' * 5}Max Marks{' ' * 5}Marks Obtained{' ' * 5}Percentage"
            )
            count = 1
            while True:
                data = pickle.load(resultFile)

                window.print(
                    f"{count}. {str(data['sub'])}{' ' * (12 - len(data['sub']))}{data['total']}{' ' * (14 - len(str(data['total'])))}{data['score']}{' ' * (19 - len(str(data['score'])))}{data['perc']}"
                )
                count += 1
        except EOFError:
            window.print("\nComplete..", color=COLORS.LIGHT_GREEN)
            window.input(
                "Press any key to return...", color=COLORS.LIGHT_RED, canBeEmpty=True
            )
            window.rerender()

    except FileNotFoundError:
        window.print(
            "\nYou haven't saved any results yet.\nREDIRECTING...",
            color=COLORS.LIGHT_BLUE,
        )
        time.sleep(2)
        window.rerender()

    except Exception as E:
        window.print(str(E))
        window.quit()
