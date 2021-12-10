"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active;
small hydrothermal vents release smoke into the caves that slowly settles like
rain.

If you can model how the smoke flows through the caves, you might be able to
avoid it and be that much safer. The submarine generates a heightmap of the
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the
following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than
any of its adjacent locations. Most locations have four adjacent locations
(up, down, left, and right); locations on the edge or corner of the map have
three or two adjacent locations, respectively. (Diagonal locations do not
count as adjacent.)

In the above example, there are four low points, all highlighted: two are in
the first row (a 1 and a 0), one is in the third row (a 5), and one is in the
bottom row (also a 5). All other locations on the heightmap have some lower
adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the
risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels
of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk
levels of all low points on your heightmap?


--- Part Two ---
Next, you need to find the largest basins so you know what areas are most
important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the
low point. The example above has four basins.

The top-left basin, size 3:
2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:
2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:
2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:
2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above
example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest
basins?
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


def generate_heightmap_image(heightmap: list[list[int]]):
    image = Image.new('RGBA', (len(heightmap[0]), len(heightmap)),  (0, 0, 0, 255))
    pixels = image.load()
    for i in range(9):
        for r_i, row in enumerate(heightmap):
            for c_i, column in enumerate(row):
                if column <= i:
                    r, g, b, a = image.getpixel((c_i, r_i))
                    r += 28
                    g += 28
                    b += 28
                    colo = (r, g, b, a)
                    pixels[c_i, r_i] = colo

    #image = enlarge_image(image, len(heightmap[0]), len(heightmap), base=4096)
    filepath = (f'Day_09/image.png')
    image.save(filepath)


def format_data(in_file: TextIOWrapper) -> list[list[int]]:
    """Return a list of list[int] from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[list[int]]: input data as list[list[int]]
    """

    output = []
    for line in [x.strip() for x in in_file.readlines()]:
        output.append([int(x) for x in line])
    return output


def get_risk_and_low_points(heightmap: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    """For the given 'n' x 'm' heightmap. Check the vertical
    and horizontal neighbors of each location in the map.
    If the neighbors are all higher (greater than) the
    location, calculate the risk level by adding 1 to the
    height of that location. Sum all of the risk levels.

    Args:
        heightmap (list[list[int]]): the heightmap; 9 is high, 0 is low.

    Returns:
        tuple[int, list[tuple[int, int]]] Total risk level, list of low points (x, y)
    """

    risk = 0
    low_points = []
    for r_i, row in enumerate(heightmap):
        for c_i, column in enumerate(row):
            neighbors = get_neighbors(heightmap, r_i, c_i)

            if column < min([heightmap[n[0]][n[1]] for n in neighbors]):
                risk += column + 1
                low_points.append((r_i, c_i))
    return risk, low_points


def get_neighbors(heightmap: list[list[int]], column: int, row: int) -> list[tuple[int, int]]:
    """Return all direct horizontal and vertical neighbors
    for a given row, column in the heightmap as a list.

    Args:
        heightmap (list[list[int]]): The heightmap
        column (int): index of the column
        row (int): index of the row

    Returns:
        list[tuple[int, int]]: neighbors (x, y)
    """

    neighbors = []
    for i in [-1, 1]:
        # check left and right
        if column + i >= 0 and column + i < len(heightmap):
            neighbors.append((column + i, row))

        # check up and down
        if row + i >= 0 and row + i < len(heightmap[0]):
            neighbors.append((column, row + i))

    return neighbors


def get_basins_recursive(heightmap: list[list[int]], coords: tuple[int, int], visited: list[tuple[int, int]]) -> int:
    """Get every neighbor of the passed coordinates. If
    we have not yet visited that neighbor, mark it as visited.
    If the value of that neighbor is smaller than 9, add
    pass its coordinates back into the recursive method to check
    its neighbors, etc.

    Sum the size of each returned value and finally return.

    Args:
        heightmap (list[list[int]]): the heightmap.
        coords (tuple[int, int]): the initial coordinates to check around.
        visited (list[tuple[int, int]]): list of all previously visited locations.

    Returns:
        int: total number of locations in the basin.
    """

    basin_size = 1
    for neighbor_x, neighbor_y in get_neighbors(heightmap, coords[0], coords[1]):
        if (neighbor_x, neighbor_y) not in visited:
            visited.append((neighbor_x, neighbor_y))
            if heightmap[neighbor_x][neighbor_y] != 9:
                basin_size += get_basins_recursive(heightmap, (neighbor_x, neighbor_y), visited)
    return basin_size


def get_prod_of_three_large_basins(heightmap: list[list[int]], lows: list[tuple[int, int]]) -> int:
    """Find all the the basins in the heightmap. Return the product of the size of the
    three largest basins.

    Args:
        heightmap (list[list[int]]): the heightmap
        lows (list[tuple[int, int]]): list of all the low points.

    Returns:
        int: product of thee largest basins
    """

    basins = []
    visited = []
    for low_x, low_y in lows:
        visited.append((low_x, low_y))
        basins.append(get_basins_recursive(heightmap, (low_x, low_y), visited))
    basins.sort()
    return basins[-3] * basins[-2] * basins[-1]


if __name__ == "__main__":
    with open("Day_09/input.txt", "r", encoding="utf-8") as f:
        data = format_data(f)
    generate_heightmap_image(data)

    # rl, lp = get_risk_and_low_points(data)
    # print(f"# Part 1: {rl:6}")
    # print(f"# Part 2: {get_prod_of_three_large_basins(data, lp):6}")

# Part 1:    541
# Part 2: 847504
