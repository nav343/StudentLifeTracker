import pickle
import time
from utils.colors import COLORS
from utils.window import Window


def PastResult(window: Window) -> None:
    window.rerender()
    window.print("Past Result ", color=COLORS.LIGHT_GREEN, centered=True)

    def parseResult(pathToFile: str) -> list:
        file = open(pathToFile, "rb")
        result = []
        try:
            while True:
                result.append(pickle.load(file))
        except EOFError:
            return result

    try:
        result = parseResult("./tests/result.dat")
        longestSubjectNameLength = max([len(x["sub"]) for x in result])
        window.print()
        window.print("─" * (window.window_size[1] - 3))
        window.print(
            f"│    │ Subject{' ' * (5 if longestSubjectNameLength < 12 else (longestSubjectNameLength - 7 + 2))}│ Max Marks{' ' * 5}│ Marks Obtained{' ' * 5}│ Percentage",
            color=COLORS.LIGHT_GREEN,
        )
        count = 1
        window.print("─" * (window.window_size[1] - 3))
        for data in result:
            name = (
                str(data["sub"])
                if len(data["sub"]) < 20
                else str(data["sub"])[:20] + "..."
            )
            window.print(
                # f"{count}. {name}{' ' * (12 - len(data['sub']) if longestSubjectNameLength < 12 else (longestSubjectNameLength + 2 - len(data['sub'])))}{data['total']}{' ' * (14 - len(str(data['total'])))}{data['score']}{' ' * (19 - len(str(data['score'])))}{data['perc']}"
                f"│ {count}. │ {name}{' ' * (12 - len(name) if longestSubjectNameLength < 12 else (longestSubjectNameLength - len(name)))}│ {data['total']}{' ' * (14 - len(str(data['total'])))}│ {data['score']}{' ' * (19 - len(str(data['score'])))}│ {data['perc']}"
            )
            window.print("─" * (window.window_size[1] - 3))
            count += 1

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
