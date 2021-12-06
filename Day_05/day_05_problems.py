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

from PIL import Image


def enlarge_image(image: Image, width: int, height: int,  base: int = 512) -> Image:            # VIS: This is only for makeing an image!
    """Resize and image to scale with maximum base value.
    If base value < image dimensions, image is not resized.

    Args:
        image (Imgae): image to resize
        width (int): width of image
        height (int): height of image
        base (int, optional): max image size. Defaults to 512.

    Returns:
        Image: the enlarged image
    """

    scale = max(width, height, base) / max(width, height)
    return image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)


def make_png(diagram: list[list[int]], i) -> None:                                              # VIS: This is only for makeing an image!
    """Generate am image of the given diagram.

    Args:
        diagram (list[list[int]]): The diagram
    """

    image = Image.new('RGB', (len(diagram[0]), len(diagram)),  (0, 0, 0))
    pixels = image.load()
    for c_i, column in enumerate(diagram):
        for r_i, row in enumerate(column):
            cell_color = (row * 90, 10, 10) if row != 0 else (0, 0, 0)
            pixels[c_i, r_i] = cell_color
    # image = enlarge_image(image, len(diagram[0]), len(diagram), base=4096)                    # VIS: This is only for makeing an image!
    filepath = (f'Day_05/images/image_{i}.png')
    image.save(filepath)


def print_diagram(diagram: list[list[int]]) -> None:
    """Print the diagram to the terminal

    Args:
        diagram (list[list[int]]): The diagram
    """

    _ = [print(*[x if x > 0 else "." for x in row], end="\n") for row in diagram]


def format_data(in_file: TextIOWrapper) -> list[list[int]]:
    """Return a list of int from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[list[int]]: input data as list of line segments
    """

    _ = [int(z) for x in in_file.readlines() for y in x.strip().replace(" -> ", ",").split() for z in y.split(",")]
    return [_[i: i + 4] for i in range(0, len(_), 4)]


def make_diagram(initial_data: list[list[int]]) -> list[list[int]]:
    """Given a list of points (x1, y1, x2, y2, ... xn, yn),
    construct an n by n list of list[int] to represent a
    diagram that will hold all points. Fill each spot with
    a 0 to begin.

    Args:
        initial_data (list[list[int]]): initial list of points

    Returns:
        list[list[int]]: diagram
    """

    width, height = max(max(_[:: 2]) for _ in initial_data), max(max(_[1:: 2]) for _ in initial_data)
    diagram = [[0 for _ in range(height + 1)] for _ in range(width + 1)]
    return diagram


def mark_horizontal_vertical_points(points: list[int], diagram: list[list[int]], i) -> list[list[int]]:  # VIS: This is only for makeing an image! (the *** i *** specifically)
    """For the given list of 4 points (x1, y1, x2, y2) line segment,
    add 1 to each point in the diagram the line segments include.

    Only consider horizontal and vertical line segments.


    Args:
        points (list[int]): start and end of line segment
        diagram (list[list[int]]): initial diagram

    Returns:
        list[list[int]]: marked diagram
    """

    x_1, y_1, x_2, y_2 = points

    # Horizontal
    if x_1 == x_2:
        i += 1                                                                                  # VIS: This is only for makeing an image! (the *** i *** specifically)
        y_min, y_max = min(y_1, y_2), max(y_1, y_2) + 1
        for y_i in range(y_min, y_max):
            diagram[y_i][x_1] += 1
    # Vertical
    if y_1 == y_2:
        i += 1                                                                                  # VIS: This is only for makeing an image! (the *** i *** specifically)
        x_min, x_max = min(x_1, x_2), max(x_1, x_2) + 1
        for x_i in range(x_min, x_max):
            diagram[y_1][x_i] += 1
    return diagram, i                                                                           # VIS: This is only for makeing an image! (the *** i *** specifically)


def mark_diagonal_points(points: list[int], diagram: list[list[int]], i) -> list[list[int]]:    # VIS: This is only for makeing an image! (the *** i *** specifically)
    """For the given list of 4 points (x1, y1, x2, y2) line segment,
    add 1 to each point in the diagram the line segments include.

    Only consider vertical lines.


    Args:
        points (list[int]): start and end of line segment
        diagram (list[list[int]]): initial diagram

    Returns:
        list[list[int]]: marked diagram
    """

    x_1, y_1, x_2, y_2 = points
    y_min, y_max = min(y_1, y_2), max(y_1, y_2)
    x_min, x_max = min(x_1, x_2), max(x_1, x_2)

    try:
        slope = (y_2 - y_1) / (x_2 - x_1)
    except ZeroDivisionError:
        slope = 0

    if slope == 1:
        i += 1                                                                                  # VIS: This is only for makeing an image! (the *** i *** specifically)
        for _ in range(0, x_max - x_min + 1):
            diagram[y_min + _][x_min + _] += 1
    elif slope == -1:
        i += 1                                                                                  # VIS: This is only for makeing an image! (the *** i *** specifically)
        for _ in range(0, x_max - x_min + 1):
            diagram[y_max - _][x_min + _] += 1
    return diagram, i                                                                           # VIS: This is only for makeing an image! (the *** i *** specifically)


def find_dangerous_areas(diagram: list[list[int]]) -> int:
    """For the given marked diagram, calculate the total
    number of points  where at least two lines overlap
    i.e. The value is >= 2

    Args:
        diagram (list[list[int]]): marked diagram

    Returns:
        int: sum of points > 1
    """

    total = sum(1 for row in diagram for x in row if x > 1)
    return total


def main(line_segments: list[list[int]]) -> tuple[int, int]:
    """Return the result of checking all horizontal and
    vertical line segments as part 1.
    Return the result of then checking the diagonal line
    segments as part 2.

    Args:
        initial_data (list[list[int]]): the initial input data

    Returns:
        tuple[int, int]: results for part 1 and part 2
    """

    diagram = make_diagram(line_segments)
    i = -1                                                                                      # VIS: This is only for makeing an image! (the *** i *** specifically)
    for points in line_segments:
        diagram, i = mark_horizontal_vertical_points(points, diagram, i)                        # VIS: This is only for makeing an image! (the *** i *** specifically)
        # noqa E501                                                                             # VIS: For anmimated gif, put diagram, i = mark_diagonal_points(points, diagram, i) here too. then call make_png(diagram, i)
        # make_png(diagram, i)                                                                  # VIS: This is only for makeing an image! (the *** i *** specifically)
    part_1 = find_dangerous_areas(diagram)

    for points in line_segments:
        diagram, i = mark_diagonal_points(points, diagram, i)                                   # VIS: This is only for makeing an image! (the *** i *** specifically)
    part_2 = find_dangerous_areas(diagram)
    make_png(diagram, i)                                                                      # VIS: For single image, only call make_png(diagram, i) here, and not above.

    return part_1, part_2


if __name__ == "__main__":
    with open("Day_05/input.txt", "r", encoding="utf-8") as f:
        data = format_data(f)

p1, p2 = main(data)
print(f"Part 1: {p1:5}")
print(f"Part 2: {p2:5}")

# Part 1:  6572
# Part 2: 21466
