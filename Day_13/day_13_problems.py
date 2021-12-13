"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you
could do some kind of thermal imaging so you could tell ahead of time which
caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you
activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.

Apparently, the Elves have never used this feature. To your surprise, you
manage to find the manual; as you go to open it, page 1 falls out. It's a
large sheet of transparent paper! The transparent paper is marked with random
dots and includes instructions on how to fold it up (your puzzle input). For
example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

The first section is a list of dots on the transparent paper. 0,0 represents
the top-left coordinate.  The first value, x, increases to the right.  The
second value, y, increases downward.  So, the coordinate 3,0 is to the right
of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example
form the following pattern, where # is a dot on the paper and . is an empty,
unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Then, there is a list of fold instructions. Each instruction indicates a line
on the transparent paper and wants you to fold the paper up (for horizontal
y=... lines) or left (for vertical x=... lines). In this example, the first
fold instruction is fold along y=7, which designates the line formed by all of
the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Because this is a horizontal line, fold the bottom half up. Some of the dots
might end up overlapping after the fold is complete, but dots will never
appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........

Now, only 17 dots are visible.
Notice, for example, the two dots in the bottom left corner before the
transparent paper is folded; after the fold is complete, those dots appear in
the top left corner (at 0,0 and 0,1). Because the paper is transparent, the
dot just below them in the result (at 0,3) remains visible, as it can be seen
through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge
together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:
#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....

Because this is a vertical line, fold left:
#####
#...#
#...#
#...#
#####
.....
.....

The instructions made a square!
The transparent paper is pretty big, so for now, focus on just completing the
first fold. After the first fold in the example above, 17 dots are visible -
dots that end up overlapping after the fold is completed count as a single
dot.

How many dots are visible after completing just the first fold instruction on
your transparent paper?


--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual
says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

"""


from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> tuple[list[list[int]], list[tuple[str, int]]]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        tuple[list[list[int]], list[tuple[str, int]]]: [x,y] coordinates, (axis, distance) folds
    """

    coordinates = []
    fold_instructions = []
    for line in in_file.readlines():
        line = line.strip()
        if line.startswith("fold"):
            fold_axis_distance = line.split("=")
            fold_instructions.append((fold_axis_distance[0][-1], int(fold_axis_distance[1])))
        elif len(line) > 1:
            coord = line.split(",")
            coordinates.append([int(coord[0]), int(coord[1])])
    return coordinates, fold_instructions


def make_grid(points: list[list[int]]) -> list[list[str]]:
    """Given a list of x,y coordinates, make a grid that
    can hold all points and populate the given set of points
    with "█".

    Args:
        points (list[list[int]]): the list of points

    Returns:
        list[list[str]]: populated grid
    """

    max_x = max([x[0] for x in points]) + 1
    max_y = max([x[1] for x in points]) + 1
    return [["█" if [x, y] in points else " " for x in range(max_x)] for y in range(max_y)]


def print_grid(printable_grid: list[list[str]]) -> None:
    """Print the grid

    Args:
        printable_grid (list[list[str]]): the grid
    """

    print()
    for row in printable_grid:
        for column in row:
            print(column, end="")
        print()
    print()


def fold_paper(unfolded_paper: list[list[str]], fold_line: tuple[str, int]) -> list[list[str]]:
    """Fold the paper on the given axis

    Args:
        unfolded_paper (list[list[str]]): the paper
        fold_line (tuple[str, int]): axis, value Ex: ('x', 5)

    Returns:
        list[list[str]]: folded paper
    """

    axis, amount = fold_line
    if axis == "y":
        for i, x in enumerate(unfolded_paper):
            for j, _ in enumerate(x):
                row = i
                if i > amount:
                    row = 2 * amount - i
                unfolded_paper[row][j] = "█" if unfolded_paper[i][j] == "█" else unfolded_paper[row][j]
        return unfolded_paper[:amount]

    for i, x in enumerate(unfolded_paper):
        for j, _ in enumerate(x):
            col = j
            if j > amount:
                col = 2 * amount - j
            unfolded_paper[i][col] = "█" if unfolded_paper[i][j] == "█" else unfolded_paper[i][col]
    for i, x in enumerate(unfolded_paper):
        unfolded_paper[i] = unfolded_paper[i][:amount]
    return unfolded_paper


def count_dots(folded_paper: list[list[str]]) -> int:
    """Count all the populated spots in the paper

    Args:
        folded_paper (list[list[str]]): the paper

    Returns:
        int: sum of all populated spots
    """

    return sum(1 for row in folded_paper for column in row if column == "█")


if __name__ == "__main__":
    with open("Day_13/sample.txt", "r", encoding="utf-8") as f:
        coords, folds = format_data(f)
    grid = make_grid(coords)
    paper = fold_paper(grid, folds[0])
    p1 = count_dots(paper)
    for fold in folds[1:]:
        paper = fold_paper(paper, fold)
    print(f"# Part 1: {p1}")
    print("# Part 2:")
    print_grid(grid)

# Part 1: 592
# Part 2:
#
#   ██  ██   ██    ██ ████ ████ █  █ █  █
#    █ █  █ █  █    █ █    █    █ █  █  █
#    █ █    █  █    █ ███  ███  ██   █  █
#    █ █ ██ ████    █ █    █    █ █  █  █
# █  █ █  █ █  █ █  █ █    █    █ █  █  █
#  ██   ███ █  █  ██  ████ █    █  █  ██
