"""Bunch of colors and other helpful codes for the terminal."""


__ESC__ = "\033["
"""ASCII escape character \\033["""


_bl_ = 30
"""black text 30m"""

_r_ = 31
"""red text 31m"""

_g_ = 32
"""green text 32m"""

_y_ = 33
"""yellow text 33m"""

_b_ = 34
"""blue text 34m"""

_m_ = 35
"""magenta text 35m"""

_c_ = 36
"""cyan text 36m"""

_w_ = 37
"""white text 37m"""

_d_ = 39
"""default text color 39m"""


# text bright
_bl_br_ = 90
"""bright black 90m"""

_r_br_ = 91
"""bright red 91m"""

_g_br_ = 92
"""bright green 92m"""

_y_br_ = 93
"""bright yellow 93m"""

_b_br_ = 94
"""bright blue 94m"""

_m_br_ = 95
"""bright magenta 95m"""

_c_br_ = 96
"""bright cyan 96m"""

_w_br_ = 97
"""bright white 97m"""


# background
_bl_bg_ = 40
"""black background 40m"""

_r_bg_ = 41
"""red background 41m"""

_g_bg_ = 42
"""green background 42m"""

_y_bg_ = 43
"""yellow background 43m"""

_b_bg_ = 44
"""blue background 44m"""

_m_bg_ = 45

"""magenta background 45m"""
_c_bg_ = 46
"""cyan background 36m"""

_w_bg_ = 47
"""white background 47m"""

_d_bg_ = 49
"""default background color 49m"""


# background bright
_bl_br_bg_ = 100
"""bright black background 100m"""

_r_br_bg_ = 101
"""bright red background 101m"""

_g_br_bg_ = 102
"""bright green background 102m"""

_y_br_bg_ = 103
"""bright yellow background 103m"""

_b_br_bg_ = 104
"""bright blue background 104m"""

_m_br_bg_ = 105
"""bright magenta background 105m"""

_c_br_bg_ = 106
"""bright cyan background 106m"""

_w_br_bg_ = 107
"""bright white background 107m"""


_bold_ = 1
"""bold text on 1m"""

_n_bold_ = 21
"""bold text off 21m"""

_dim_ = 2
"""dim text on 2m"""

_n_dim_ = 22
"""dim text off 22m"""

_italic_ = 3
"""italic text on 3m"""

_n_italic_ = 23
"""italic text off 23m"""

_underline_ = 4
"""underline text on 4m"""

_n_underline_ = 24
"""underline text off 24m"""

_slow_blink_ = 5
"""slow blink on 5m"""

_n_slow_blink_ = 25
"""slow blink off 25m"""

_rapid_blink_ = 6
"""rapid blink on 6m"""

_n_rapid_blink_ = 26
"""rapid blink off 26m"""

_strike_through_ = 9
"""strikethrugh text on 9m"""

_n_strike_through_ = 29
"""strike-through text off 29m"""


_reset_ = 0
"""reset all styles 0m"""

_inv_ = "?25l"
"""cursor invisible ?25l"""

_visible_ = "?25h"
"""cursor visible ?25h"""

_hide_ = 8
"""hide text 8m"""

_home_ = "H"
"""move to home position (1,1 or 0,0) H"""


# Text
BLACK = f"{__ESC__}30m"
"""Black text 30m"""

RED = f"{__ESC__}31m"
"""Red text 31m"""

GREEN = f"{__ESC__}32m"
"""Green text 32m"""

YELLOW = f"{__ESC__}33m"
"""Yellow text 33m"""

BLUE = f"{__ESC__}34m"
"""Blue text 34m"""

MAGENTA = f"{__ESC__}35m"
"""Magenta text 35m"""

CYAN = f"{__ESC__}36m"
"""Cyan text 36m"""

WHITE = f"{__ESC__}37m"
"""White text 37m"""

DEFAULT = f"{__ESC__ }39m"
"""Default text color 39m"""


# Text bright
BLACK_BR = f"{__ESC__}90m"
"""Bright black 90m"""

RED_BR = f"{__ESC__}91m"
"""Bright red 91m"""

GREEN_BR = f"{__ESC__}92m"
"""Bright green 92m"""

YELLOW_BR = f"{__ESC__}93m"
"""Bright yellow 93m"""

BLUE_BR = f"{__ESC__}94m"
"""Bright blue 94m"""

MAGENTA_BR = f"{__ESC__}95m"
"""Bright magenta 95m"""

CYAN_BR = f"{__ESC__}96m"
"""Bright cyan 96m"""

WHITE_BR = f"{__ESC__}97m"
"""Bright white 97m"""


# Background
BLACK_BG = f"{__ESC__}40m"
"""Black background 40m"""

RED_BG = f"{__ESC__}41m"
"""Red background 41m"""

GREEN_BG = f"{__ESC__}42m"
"""Green background 42m"""

YELLOW_BG = f"{__ESC__}43m"
"""Yellow background 43m"""

BLUE_BG = f"{__ESC__}44m"
"""Blue background 44m"""

MAGENTA_BG = f"{__ESC__}45m"

"""Magenta background 45m"""
CYAN_BG = f"{__ESC__}46m"
"""Cyan background 36m"""

WHITE_BG = f"{__ESC__}47m"
"""White background 47m"""

DEFAULT_BG = f"{__ESC__ }49m"
"""Default background color 49m"""


# Background bright
BLACK_BR_BG = f"{__ESC__}100m"
"""Bright black background 100m"""

RED_BR_BG = f"{__ESC__}101m"
"""Bright red background 101m"""

GREEN_BR_BG = f"{__ESC__}102m"
"""Bright green background 102m"""

YELLOW_BR_BG = f"{__ESC__}103m"
"""Bright yellow background 103m"""

BLUE_BR_BG = f"{__ESC__}104m"
"""Bright blue background 104m"""

MAGENTA_BR_BG = f"{__ESC__}105m"
"""Bright magenta background 105m"""

CYAN_BR_BG = f"{__ESC__}106m"
"""Bright cyan background 106m"""

WHITE_BR_BG = f"{__ESC__}107m"
"""Bright white background 107m"""


BOLD = f"{__ESC__}1m"
"""Bold text on 1m"""

N_BOLD = f"{__ESC__}21m"
"""Bold text off 21m"""

DIM = f"{__ESC__}2m"
"""Dim text on 2m"""

N_DIM = f"{__ESC__}22m"
"""Dim text off 22m"""

ITALIC = f"{__ESC__}3m"
"""Itallic text on 3m"""

N_ITALIC = f"{__ESC__}23m"
"""Itallic text off 23m"""

UNDERLINE = f"{__ESC__}4m"
"""Underline text on 4m"""

N_UNDERLINE = f"{__ESC__}24m"
"""Underline text off 24m"""

SLOW_BLINK = f"{__ESC__}5m"
"""Slow blink on 5m"""

N_SLOW_BLINK = f"{__ESC__}25m"
"""Slow blink off 25m"""

RAPID_BLINK = f"{__ESC__}6m"
"""Rapid blink on 6m"""

N_RAPID_BLINK = f"{__ESC__}26m"
"""Rapind blink off 26m"""

STRIKE_THROUGH = f"{__ESC__}9m"
"""Strikethrugh text on 9m"""

N_STRIKE_THROUGH = f"{__ESC__}29m"
"""Strikethrough text off 29m"""


RESET = f"{__ESC__}0m"
"""Reset all styles 0m"""

INV = f"{__ESC__}?25l"
"""Curser invisible ?25l"""

VISIBLE = f"{__ESC__}?25h"
"""Curser visible ?25h"""

HIDE = f"{__ESC__}8m"
"""Hide text 8m"""

HOME = f"{__ESC__}H"
"""Move to home position (1,1 or 0,0) H"""


def RGB(r: int | str, g: int | str, b: int | str) -> str:
    """change the text to an rgb color.

     Note:
        Values from 0 - 255

    Args:
        r (int|str): 0-255 value for red
        g (int|str): 0-255 value for green
        b (int|str): 0-255 value for blue

    Returns:
        str: ESC 38;2;<r>;<g>;<b>m
    """

    return f"{__ESC__}38;2;{r};{g};{b}m"


RGB_RED = RGB(255, 0, 0)
"""Calls RGB(255, 0, 0)"""

RBG_ORANGE = RGB(255, 127, 0)
"""Calls RGB(255, 127, 0)"""

RGB_YELLOW = RGB(255, 255, 0)
"""Calls RGB(255, 255, 0)"""

RGB_GREEN = RGB(0, 255, 0)
"""Calls  RGB(0, 255, 0)"""

RGB_BLUE = RGB(0, 0, 255)
"""Calls RGB(0, 0, 255)"""

RGB_INDIGO = RGB(75, 0, 130)
"""Calls RGB(75, 0, 130)"""

RGB_VIOLET = RGB(148, 0, 211)
"""Calls RGB(148, 0, 211)"""


def RGB_BG(r: int | str, g: int | str, b: int | str) -> str:
    """Change the background to an RGB color.

    Note:
        Values from 0 - 255

    Args:
        r (int|str): 0-255 value for red
        g (int|str): 0-255 value for green
        b (int|str): 0-255 value for blue

    Returns:
        str: ESC 48;2;<r>;<g>;<b>m
    """

    return f"{__ESC__}48;2;{r};{g};{b}m"


def COLOR_256(value: int | str) -> str:
    """Change text to 1 of 256 colors.

    Args:
        value (int|str): 0 - 255

    Returns:
        str: ESC 38;5;<c>m
    """

    return f"{__ESC__}38;5;{value}m"


def COLOR_256_BG(value: int | str) -> str:
    """Change background to 1 of 256 colors.

    Args:
        value (int|str): 0 - 255

    Returns:
        str: ESC 48;5;<c>m
    """

    return f"{__ESC__}48;5;{value}m"


def MOVE(rows: int | str, columns: int | str) -> str:
    """Move the curser to row, column.

    Args:
        rows (int | str): The row
        columns (int | str): The column

    Returns:
        str: ESC<row>;<column>H
    """

    return f"{__ESC__}{rows};{columns}H"


def UP(lines: int | str) -> str:
    """Move up by # of lines

    Args:
        lines (int | str): # of lines to move up

    Returns:
        str: ESC<lines>A
    """

    return f"{__ESC__}{lines}A"


def DOWN(lines: int | str) -> str:
    """Move down by # of lines

    Args:
        lines ([type]): # of lines to move down

    Returns:
        str: ESC<lines>B
    """

    return f"{__ESC__}{lines}B"


def RIGHT(columns: int | str) -> str:
    """Move right by # of columns

    Args:
        lines (int | str): # of columns to move right

    Returns:
        str: ESC<columns>C
    """

    return f"{__ESC__}{columns}C"


def LEFT(columns: int | str) -> str:
    """Move left by # of columns

    Args:
        lines (int | str): # of columns to move left

    Returns:
        str: ESC<columns>D
    """

    return f"{__ESC__}{columns}D"


def START_DOWN(amount: int | str) -> str:
    """Moves cursor to beginning of next line, # lines down

    Args:
        amount (int | str): # to move down

    Returns:
        str: ESC<amount>E
    """

    return f"{__ESC__}{amount}E"


def START_UP(amount: int | str) -> str:
    """Moves cursor to beginning of previous line, # lines up

    Args:
        amount (int | str): # to move up

    Returns:
        str: ESC<amount>F
    """

    return f"{__ESC__}{amount}F"


def MOVE_TO_COLUMN(column: int | str) -> str:
    """Moves cursor to column #

    Args:
        column (int): Column # to move to

    Returns:
        str: ESC<column>G
    """

    return f"{__ESC__}{column}G"


def CHAIN_SEQUENCE(*args: str | int) -> str:
    """Pass in any number of valid escape sequences and get
    a formatted string with all the commands seperated by ;

    Note:
        can be used if you want to change many things at once
        but do not need to call each one idividually.

    Returns:
        str: ESC<n1>;<n2>;...<n>m
    """

    chained_commands = ";".join(str(a) for a in args)
    return f"{__ESC__}{chained_commands}m"


if __name__ == "__main__":
    print(f"Testing commands: 1, 3, 30, 47:\n{CHAIN_SEQUENCE(1,3,30,47)}Test text should be bold, itallic, black with white background.{RESET}")

    color_256 = "\n\t\t************** COLOR 256 **************"
    for i, c in enumerate(color_256):
        print(f"{COLOR_256(i)}{c}", end='')

    print('\n')
    for i in range(256):
        if i == 0:
            print("    ", end='')
        if i == 16:
            print()
        if (i-16) % 24 == 0 and 0 != i > 15:
            print('', end='')
        if (i-16) % 6 == 0 and 0 != i > 15:
            print("", end='\t')
        if (i-16) % 12 == 0 and 0 != i > 15:
            print("\n", end='\t')
        print(f"{BOLD}{COLOR_256(i)}{i:4}", end='')
    print(RESET+'\n')

    color_256_bg = "\n\t\t********** COLOR 256 BG **********"
    for i, c in enumerate(color_256_bg):
        print(f"{COLOR_256(i)}{c}", end='')

    print(RESET+'\n')
    for i in range(256):
        if i == 0:
            print(RESET+"    ", end='')
        if i == 16:
            print(RESET)
        if (i-16) % 24 == 0 and i > 15:
            print(RESET, end='')
        if (i-16) % 6 == 0 and i > 15:
            print(RESET, end='\t')
        if (i-16) % 12 == 0 and 0 != i > 15:
            print(RESET+"\n", end='\t')
        print(f"{COLOR_256(i)}{COLOR_256_BG(i)}{i:4}", end='')
    print(RESET+'\n')
