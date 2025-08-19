import os

if os.name == "posix":
    import readline

import sys
import time

from .colors import COLORS, TextColor


class Window:
    """
    Window base class.
    Initialises a window (buffer) of the same size as the size of terminal window
    A buffer is a list containing every element (sub-buffers) to be displayed
    Upon intialisation, a box is drawn (first and last line containing '-' and all lines in between made of '\\n) around the terminal window and a position pointer is set to (1,1) (i.e First line, First column)'
    Various methods of this class uses the position pointer to replace the blank sub-buffers with the desired text
    """

    window_size: tuple[int, int]
    """Get or set the size of window buffer.

    Usage: window_size -> (_lines, _columns)

    `Window.window_size` -> Returns the size of window (defaults to size of the terminal)

    `Window.window_size = (lines, columns)` -> Sets the size of window to given value
    """

    __buffer: list
    __pos: tuple[int, int]
    __clear = "cls" if os.name == "nt" else "clear"
    __slots: int

    def __init__(self) -> None:
        os.system(self.__clear)
        self.window_size = (
            os.get_terminal_size().lines - 1,
            os.get_terminal_size().columns,
        )
        self.__buffer = []
        self.__pos = (0, 0)
        self.__set_buffer()
        self.__slots: int = self.window_size[0]

    def __set_buffer(self):
        self.__buffer.append(f"┌{'─' * (self.window_size[1] - 2)}┐")
        for _ in range(self.window_size[0] - 2):
            self.__buffer.append(self.__format(TextColor(" ")))
        self.__buffer.append(f"└{'─' * (self.window_size[1] - 2)}┘")
        self.__pos = (1, 1)

    def __format(
        self, msg: str, centered: bool = False, rightAlign: bool = False
    ) -> str:
        # return f"│{' ' * (1 if not centered else self.window_size[1] // 2 - len(msg) // 2 + 5)}{msg}{' ' * (self.window_size[1] - len(msg) + 8 if not centered else self.window_size[1] // 2 - len(msg) // 2 + 3)}│"
        lenMessageWithoutColor = msg[11:-5]
        partialText = (
            f"│{' ' * (1 if not centered else (self.window_size[1] // 2 - len(lenMessageWithoutColor) // 2 - 1))}{msg}"
            if not rightAlign
            else f"│{' ' * (self.window_size[1] - len(msg) + 8)}{msg}"
        )
        # Needs some work here, I have no idea where that ... + 10 is coming from (got it by hit and trial, seems to be working with 10)
        return f"{partialText}{' ' * (self.window_size[1] - len(partialText) + 10 if not rightAlign else 1)}│"

    def __breakChunk(self, msg: str) -> list:
        res = []
        a = self.window_size[1] - 5
        for i in range(len(msg) // a + 1):
            res.append(msg[i * a : (i + 1) * a])
        return res

    # Public functions

    def refresh(self) -> None:
        """
        Pushes buffer into the system terminal

        Returns None
        """
        os.system(self.__clear)
        for i in self.__buffer:
            print(i)

    def print(
        self,
        msg: str = " ",
        centered: bool = False,
        color: str = COLORS.LIGHT_WHITE,
        rightAlign: bool = False,
        verticalCenter: bool = False,
        endSpace: bool = False,
    ) -> None:
        """
        The one and only method for writing text to the Window buffer

        Architecture:
        Writes text line by line to the buffer

        `msg`: str - The text you want to print
        `centered`: bool - Whether the text is to be centered horizontally. Defaulst to False
        `color`: COLORS - Color of your text. Defaults to LIGHT_WHITE
        `verticalCenter`: bool - Whether the text is to be centered vertically. Defaults to False
            Note: Make sure to call `window.rerender()` if set to True
        `endSpace`: bool - Whether to add a blank line after message (Defaults to False)

        Returns None
        """
        if len(msg) < self.window_size[1] and self.__slots > len(msg.split("\n")):
            for i in msg.split("\n"):
                self.__buffer[
                    self.__pos[0] if not verticalCenter else self.window_size[0] // 2
                ] = self.__format(TextColor(i, color), centered, rightAlign)
                if verticalCenter:
                    self.__pos = (self.window_size[0] // 2 + 1, self.__pos[1])
                else:
                    self.__pos = (self.__pos[0] + 1, self.__pos[1])
                self.__slots -= 1
                self.refresh()
        elif len(msg) > self.window_size[1] and self.__slots > len(
            self.__breakChunk(msg)
        ):
            for j in msg.split("\n"):
                for i in self.__breakChunk(j):
                    self.__buffer[self.__pos[0]] = self.__format(
                        TextColor(i, color), centered, rightAlign
                    )
                    self.__slots -= 1
                    self.__pos = (self.__pos[0] + 1, self.__pos[1])
                    self.refresh()
        elif self.__slots < self.window_size[0] // 2:
            self.rerender()
        if endSpace:
            self.__buffer[self.__pos[0]] = "\n"

    def rerender(self) -> None:
        """
        Rerenders the entire window to just the box around terminal
        Must be called if `verticalCenter` is set to True in `window.print(...)`

        Returns None
        """
        self.__buffer = []
        self.__slots = self.window_size[0]
        self.__set_buffer()

    def input(
        self,
        question: str,
        color: str = COLORS.LIGHT_WHITE,
        hidden: bool = True,
        canBeEmpty: bool = False,
        dataType: type = str,
    ):
        """
        For taking input from the user
        The `question` (or placeholder) is printed inside the window buffer but the input field is at the bottom of the terminal

        Returns the response entered by user (string type)
        """
        default_pos = self.__pos
        if not hidden:
            self.print(question, color=color)
            self.__pos = (self.__pos[0] - 1, self.__pos[1])
            res = input(">>> ")
            if (not canBeEmpty and res != "") or (canBeEmpty):
                self.__pos = default_pos
                self.print(question + res, color=color)
                return dataType(res)
            else:
                self.__pos = (self.__pos[0] + 1, self.__pos[1])
                self.print("Field cannot be empty", color=COLORS.RED)
                return dataType(
                    self.input(question, color, hidden, canBeEmpty, dataType)
                )
        else:
            self.print(question, color=color)
            return dataType(input(">>> "))

    def quit(self, clear_term: bool = False) -> None:
        """
        Closes the buffer

        `clear_term`: boolean -> Whether you want to clear the standard output (Default to False)

        Returns None
        """
        if clear_term:
            os.system(self.__clear)
        exit()

    def loader(
        self,
        char: str = "*",
        length: int = 5,
        speed: float = 0.5,
        centered: bool = False,
    ) -> None:
        """
        `char`: str - Character of your progress bar. Defaults to *
        `speed`: float - How fast the progress bar should move
        progress bar

        Returns None
        """
        progress = ""
        for i in range(length):
            progress += char
            self.__buffer[self.__pos[0]] = self.__format(
                TextColor(progress if i % 2 != 0 else progress + " "), centered
            )
            self.refresh()
            time.sleep(speed)

    def editor(self, header: str = "Editor") -> str:
        txt: str = ""
        old = self.__buffer
        self.__buffer = []
        self.__buffer.append(f"┌{'─' * (self.window_size[1] - 2)}┐")
        self.__buffer.append(
            self.__format(TextColor(header, COLORS.LIGHT_BLUE), centered=True)
        )
        self.__buffer.append("│" + " " * (self.window_size[1] - 2) + "│")
        self.__buffer.append(
            self.__format(
                TextColor(
                    f"Start typing below and {'press Ctrl-Z and hit enter' if os.name == 'nt' else 'press Ctrl-D'} to save and exit editor",
                    COLORS.YELLOW,
                )
            )
        )
        self.__buffer.append("│" + " " * (self.window_size[1] - 2) + "│")
        self.__buffer.append(f"└{'─' * (self.window_size[1] - 2)}┘")
        self.refresh()
        print(">>> ")
        txt = sys.stdin.read()
        progress = ""
        print("\n" * 2)
        for _ in range(6):
            progress += "."
            print(TextColor(f"Saving text {progress}", color=COLORS.GREEN), end="\r")
            time.sleep(0.2)
        self.__buffer = old
        self.refresh()
        return txt
