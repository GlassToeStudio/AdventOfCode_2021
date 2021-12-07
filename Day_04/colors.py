"""Bunch of colors and other helpful codes for the terminal."""

__ESC__ = '\033['

# regular
BLACK = f"{__ESC__}{'0;30'}m"  # noqa E501
RED = f"{__ESC__}{'0;31'}m"
GREEN = f"{__ESC__}{'0;32'}m"
YELLOW = f"{__ESC__}{'0;33'}m"
BLUE = f"{__ESC__}{'0;34'}m"
MAGENTA = f"{__ESC__}{'0;35'}m"
CYAN = f"{__ESC__}{'0;36'}m"
WHITE = f"{__ESC__}{'0;37'}m"

BLACK_BG = f"{__ESC__}{40}m"
RED_BG = f"{__ESC__}{41}m"
GREEN_BG = f"{__ESC__}{42}m"
YELLOW_BG = f"{__ESC__}{43}m"
BLUE_BG = f"{__ESC__}{44}m"
MAGENTA_BG = f"{__ESC__}{45}m"
CYAN_BG = f"{__ESC__}{46}m"
WHITE_BG = f"{__ESC__}{47}m"

# bright
BLACK_BR = f"{__ESC__}{'0;91'}m"
RED_BR = f"{__ESC__}{'0;92'}m"
GREEN_BR = f"{__ESC__}{'0;93'}m"
YELLOW_BR = f"{__ESC__}{'0;94'}m"
BLUE_BR = f"{__ESC__}{'0;95'}m"
MAGENTA_BR = f"{__ESC__}{'0;96'}m"
CYAN_BR = f"{__ESC__}{'0;97'}m"
WHITE_BR = f"{__ESC__}{'0;98'}m"

BLACK_BR_BG = f"{__ESC__}{100}m"
RED_BR_BG = f"{__ESC__}{101}m"
GREEN_BR_BG = f"{__ESC__}{102}m"
YELLOW_BR_BG = f"{__ESC__}{103}m"
BLUE_BR_BG = f"{__ESC__}{104}m"
MAGENTA_BR_BG = f"{__ESC__}{105}m"
CYAN_BR_BG = f"{__ESC__}{106}m"
WHITE_BR_BG = f"{__ESC__}{107}m"

BOLD = f"{__ESC__}{1}m"
ITALIC = f"{__ESC__}{3}m"
UNDERLINE = f"{__ESC__}{4}m"
SLOW_BLINK = f"{__ESC__}{5}m"
RAPID_BLINK = f"{__ESC__}{6}m"
BLINK_OFF = f"{__ESC__}{25}m"

END = f"{__ESC__}{0}m"
START = f"{__ESC__}F"
UP = f"{__ESC__}A"
HIDE = f"{__ESC__}8m"
BLINK_OFF = f"{__ESC__}{25}m"
