"""


--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
where x1,y1 are the coordinates of one end the line segment and x2,y2 are the
coordinates of the other end. These line segments include the points at both
ends. In other words:


An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 =
x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the
following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
Each position is shown as the number of lines which cover that point or . if
no line covers that point. The top-left pair of 1s, for example, comes from
2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9
and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points
where at least two lines overlap. In the above example, this is anywhere in
the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two
lines overlap?


Your puzzle answer was 6572.The first half of this puzzle is complete! It
provides one gold star: *



--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in
your list will only ever be horizontal, vertical, or a diagonal line at
exactly 45 degrees. In other words:


An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following
diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines
overlap. In the above example, this is still anywhere in the diagram with a 2
or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""


from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [int(z) for x in in_file.readlines() for y in x.strip().replace(' -> ', ',').split() for z in y.split(',')]


def check_points(points, board):
    x1 = points[0]
    x2 = points[2]
    y1 = points[1]
    y2 = points[3]
    maxy = max(y1, y2)
    miny = min(y1, y2)
    maxx = max(x1, x2)
    minx = min(x1, x2)
    slope = 0
    if (maxy - miny == maxx - minx):
        slope = 1
        if (y2-y1) * (x2-x1) < 0:
            slope = -1
    if x1 == x2:
        for z in range(miny, maxy+1):
            board[z][x1] += 1
    elif y1 == y2:
        for z in range(minx, maxx+1):
            board[y1][z] += 1
    elif slope == 1:
        for i in range(0, maxx-minx+1):
            board[miny+i][minx+i] += 1
    elif slope == -1:
        for i in range(0, maxx-minx+1):
            board[maxy-i][minx+i] += 1

    return board


def print_board(board):
    for y in range(len(board)):
        for x in range(len(board)):
            print(board[y][x] if board[y][x] > 0 else '.', end='')
        print()


def sum_2s(board):
    total = 0
    for i in range(len(board[0])):
        total += sum(1 for x in board[i] if x >= 2)
    return total


def make_board():
    board = []
    row = []
    for x in range(maximum_x+1):
        for y in range(maximum_y+1):
            row.append(0)
        board.append(row)
        row = []
    return board


if __name__ == "__main__":
    with open("Day_05/input.txt", 'r', encoding='utf-8') as f:
        data = format_data(f)
        maximum_x = max(data[::2])
        maximum_y = max(data[1::2])

        board = make_board()
        for i in range(0, len(data), 4):
            board = check_points(data[i:i+4], board)
        print_board(board)
        print(sum_2s(board))

"""
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
6377
"""
