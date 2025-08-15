from utils.colors import COLORS
from utils.window import Window


def Loader(
    window: Window,
    msg: str,
    hcenter: bool = True,
    speed: float = 0.5,
) -> None:
    window.print(msg, centered=hcenter, color=COLORS.LIGHT_BLUE)
    window.loader("*", 20, speed, centered=True)
    window.rerender()
