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
# ..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
# ..........
# .#........

Then, there is a list of fold instructions. Each instruction indicates a line
on the transparent paper and wants you to fold the paper up (for horizontal
y=... lines) or left (for vertical x=... lines). In this example, the first
fold instruction is fold along y=7, which designates the line formed by all of
the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
# ..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
# ..........
# .#........

Because this is a horizontal line, fold the bottom half up. Some of the dots
might end up overlapping after the fold is complete, but dots will never
appear exactly on a fold line. The result of doing this fold looks like this:

# .##..#..#.
# ...#......
......#...#
# ...#......
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
# .##.|#..#.
# ...#|.....
.....|#...#
# ...#|.....
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


"""


from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    coords = []
    folds = []
    for line in in_file.readlines():
        line = line.strip()
        if 1 < len(line) < 13:
            coord = line.split(',')
            coords.append([int(coord[0]), int(coord[1])])
        elif 1 < len(line):
            fold = line.split("=")
            folds.append((fold[0][-1], int(fold[1])))
    return coords, folds


def make_grid(grid):
    max_x = max([x[0] for x in grid])+1
    max_y = max([x[1] for x in grid])+1
    new_grid = []
    for y in range(max_y):
        new_grid.append(['█' if [x, y] in grid else ' ' for x in range(max_x)])
    return new_grid


def print_grid(grid):
    print()
    for row in grid:
        for column in row:
            print(column, end='')
        print()
    print()


def print_grid_to_file(grid):
    with open("Day_13/grid.txt", "w") as f:
        print("\n", file=f)
        for row in grid:
            for column in row:
                print(column, end='', file=f)
            print("\n", file=f, end='')
        print("\n", file=f)


def fold_paper(grid, fold):
    axis, amount = fold
    if axis == 'y':
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                row = i
                if i > amount:
                    row = 2*amount-i
                grid[row][j] = "█" if grid[i][j] == "█" else grid[row][j]
        return grid[:amount]

    if axis == 'x':
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                col = j
                if j > amount:
                    col = 2*amount - j
                grid[i][col] = "█" if grid[i][j] == "█" else grid[i][col]
        for i, x in enumerate(grid):
            grid[i] = grid[i][:amount]
        return grid


def count_dots(grid):
    i = 0
    for row in grid:
        for column in row:
            if column == "█":
                i += 1
    return i


if __name__ == "__main__":
    with open("Day_13/input.txt", "r", encoding='utf-8') as f:
        coords, folds = format_data(f)
    grid = make_grid(coords)
    grid = fold_paper(grid, folds[0])
    p1 = count_dots(grid)
    for fold in folds[1:]:
        grid = fold_paper(grid, fold)
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
