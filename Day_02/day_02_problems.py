"""
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.
It seems like the submarine can take a series of commands like forward 1, down
2, or up 3:


forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You
should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then
modify them as follows:


forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15
and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the
planned course. What do you get if you multiply your final horizontal position
by your final depth?
"""


from io import TextIOWrapper


def format_data(data: TextIOWrapper) -> list[str]:
    """Return a list of ints from the given text."

    Args:
        data (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """
    return [[x.strip()[0], int(x.strip()[-1])] for x in data.readlines()]


def calculate_position(course):
    h = sum(x[1] if x[0] == 'f' else 0 for x in course)
    d = sum(x[1] if x[0] == 'd' else 0 for x in course)
    d -= sum(x[1] if x[0] == 'u' else 0 for x in course)
    print(h*d)


if __name__ == "__main__":
    with open("Day_02/input.txt", "r") as in_file:
        data = format_data(in_file)
        calculate_position(data)
