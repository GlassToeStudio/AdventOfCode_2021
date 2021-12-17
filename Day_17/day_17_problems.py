"""


--- Day 17: Trick Shot ---
You finally decode the Elves' message. HI, the message says. You continue
searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys have
fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer
velocity in the x (forward) and y (upward, or downward if negative)
directions. For example, an initial x,y velocity like 0,10 would fire the
probe straight up, while an initial velocity like 10,-1 would fire the probe
forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some trajectory by
moving in steps. On each step, these changes occur in the following order:


The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is,
it decreases by 1 if it is greater than 0, increases by 1 if it is less than
0, or does not change if it is already 0.

Due to gravity, the probe's y velocity decreases by 1.

For the probe to successfully make it into the trench, the probe must be on
some trajectory that causes it to be within a target area after any step. The
submarine computer has already calculated this target area (your puzzle
input). For example:

target area: x=20..30, y=-10..-5
This target area means that you need to find initial x,y velocity values such
that after any step, the probe's x position is at least 20 and at most 30, and
the probe's y position is at least -10 and at most -5.

Given this target area, one initial velocity that causes the probe to be within
the target area after any step is 7,2:

.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT

In this diagram, S is the probe's initial position, 0,0. The x coordinate
increases to the right, and the y coordinate increases upward. In the bottom
right, positions that are within the target area are shown as T. After each
step (until the target area is reached), the position of the probe is marked
with #. (The bottom-right # is both a position the probe reaches and a
position in the target area.)

Another initial velocity that causes the probe to be within the target area
after any step is 6,3:

...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT

Another one is 9,0:
S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT

One initial velocity that doesn't cause the probe to be within the target area
after any step is 17,-4:

S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#

The probe appears to pass through the target area, but is never within it after
any step. Instead, it continues down and to the right - only the first few
steps are shown.

If you're going to fire a highly scientific probe out of a super cool probe
launcher, you might as well do it with style. How high can you make the probe
go while still reaching the target area?

In the above example, using an initial velocity of 6,9 is the best you can do,
causing the probe to reach a maximum y position of 45. (Any higher initial y
velocity causes the probe to overshoot the target area entirely.)

Find the initial velocity that causes the probe to reach the highest y position
and still eventually be within the target area after any step. What is the
highest y position it reaches on this trajectory?


"""


from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """
    xs, ys = (in_file.read().strip()[15:].replace('y=', '')).split(',')
    x1, x2 = xs.split('..')
    y1, y2 = ys.split('..')

    return (int(x1), int(x2), int(y1), int(y2))


def adjust_velocity(x, y):
    y = y - 1
    if x > 0:
        x -= 1
    if x < 0:
        x += 1
    return x, y


def in_range(x, y, target_area):
    x1, x2, y1, y2 = target_area
    return (x1 <= x <= x2 and y1 <= y <= y2)


def missed_target(x, y, target_area):
    x1, x2, y1, y2 = target_area
    if y < y1:
        return True
    if x > x2:
        return True
    return False


def try_trajectories(target_area):
    good = []
    best_ys = {}
    for _x in range(0, 1000):
        for _y in range(0, 1000):
            x = _x
            y = _y
            pos_x = 0
            pos_y = 0
            all_ys = []
            for i in range(1, 1000):
                pos_x += x
                pos_y += y
                all_ys.append(pos_y)
                #print(pos_x, pos_y)
                if in_range(pos_x, pos_y, target_area):
                    good.append((_x, _y))
                    best_ys[(_x, _y)] = max(all_ys)
                if missed_target(pos_x, pos_y, target_area):
                    break
                x, y = adjust_velocity(x, y)
    print(best_ys)
    print(good)
    k = max(best_ys, key=best_ys.get)
    print(k, best_ys[k])


if __name__ == "__main__":
    with open("Day_17/input.txt", "r", encoding='utf-8') as f:
        data = format_data(f)
        print(data)
        try_trajectories(data)


# 7, 2
# 6, 3
# 9, 0
# 6, 9
# too low 1176
