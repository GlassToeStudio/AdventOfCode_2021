"""
--- Day 23: Amphipod ---
A group of amphipods notice your fancy submarine and flag you down. "With such
an impressive shell," one amphipod says, "surely you can help us with a
question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a
nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B),
Copper (C), and Desert (D). They live in a burrow that consists of a hallway
and four side rooms. The side rooms are initially full of amphipods, and the
hallway is initially empty.

They give you a diagram of the situation (your puzzle input), including
locations of each amphipod (A, B, C, or D, each of which is occupying an
otherwise open space), walls (#), and open space (.).

For example:
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

The amphipods would like a method to organize every amphipod into side rooms so
that each side room contains one type of amphipod and the types are sorted A-D
going left to right, like this:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

Amphipods can move up, down, left, or right so long as they are moving into an
unoccupied open space. Each type of amphipod requires a different amount of
energy to move one step: Amber amphipods require 1 energy per step, Bronze
amphipods require 10 energy, Copper amphipods require 100, and Desert ones
require 1000. The amphipods would like you to find a way to organize the
amphipods that requires the least total energy.

However, because they are timid and stubborn, the amphipods have some extra
rules:


Amphipods will never stop on the space immediately outside any room. They can
move into that space so long as they immediately continue moving.
(Specifically, this refers to the four open spaces in the hallway that are
directly above an amphipod starting position.)

Amphipods will never move from the hallway into a room unless that room is
their destination room and that room contains no amphipods which do not also
have that room as their own destination. If an amphipod's starting room is not
its destination room, it can stay in that room until it leaves the room. (For
example, an Amber amphipod will not move from the hallway into the right three
rooms, and will only move into the leftmost room if that room is empty or if
it only contains other Amber amphipods.)

Once an amphipod stops moving in the hallway, it will stay in that spot until
it can move into a room. (That is, once any amphipod starts moving, any other
amphipods currently in the hallway are locked in place and will not move again
until they can move fully into a room.)


In the above example, the amphipods can be organized using a minimum of 12521
energy. One way to do this is shown below.

Starting configuration:
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

One Bronze amphipod moves into the hallway, taking 4 steps and using 40
energy:

#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########

The only Copper amphipod not in its side room moves there, taking 4 steps and
using 400 energy:

#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########

A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy,
and then the Bronze amphipod takes its place, taking 3 steps and using 30
energy:

#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########

The leftmost Bronze amphipod moves to its room using 40 energy:
#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########

Both amphipods in the rightmost room move into the hallway, using 2003 energy
in total:

#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########

Both Desert amphipods move into the rightmost room using 7000 energy:
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

Finally, the last Amber amphipod moves into its room, using 8 energy:
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

What is the least energy required to organize the amphipods?

"""

from collections import Counter
from copy import deepcopy
from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [x.strip() for x in in_file.readlines()]


if __name__ == "__main__":
    with open("Day_23/sample.txt", "r", encoding='utf-8') as f:
        data = format_data(f)
        print(data)

        #!/usr/bin/python3


#submit(len(G), part="a", day=23, year=2021)
#infile = sys.argv[1] if len(sys.argv)>1 else '23.in'
#data = open(infile).read().strip()

#############
#...........#
###B#C#A#D###
 #D#C#B#A#
 #D#B#A#C#
 #B#C#D#A#
 #########
A = ['D', 'D', 'D', 'B']
B = ['B', 'C', 'B', 'D']
C = ['A', 'B', 'A', 'A']
D = ['C', 'A', 'C', 'C']

#############
#...........#
###B#C#B#D###
#D#C#B#A#
#D#B#A#C#
#A#D#C#A#
#########
#A = ['B', 'D', 'D', 'A']
#B = ['C', 'C', 'B', 'D']
#C = ['B', 'B', 'A', 'C']
#D = ['D', 'A', 'C', 'A']

TOP = []
while len(TOP) < 11:
    TOP.append('E')
start = ({'A': A, 'B': B, 'C': C, 'D': D}, TOP)

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def done(state):
    bot, top = state
    for k, v in bot.items():
        for vv in v:
            if vv != k:
                return False
    return True


def can_move_from(k, col):
    for c in col:
        if c != k and c != 'E':
            return True
    return False


def can_move_to(k, col):
    for c in col:
        if c != k and c != 'E':
            return False
    return True


def bot_idx(bot):
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]


def top_idx(col):
    for i, c in enumerate(col):
        if c != 'E':
            return i
    return None


def dest_idx(col):
    for i, c in reversed(list(enumerate(col))):
        if c == 'E':
            return i
    return None


def between(a, bot, top):
    # 0 1 A 3 B 5 C 7 D 9 10
    return (bot_idx(bot) < a < top) or (top < a < bot_idx(bot))


assert between(1, 'A', 0)


def clear_path(bot, top_idx, top):
    for ti in range(len(top)):
        if between(ti, bot, top_idx) and top[ti] != 'E':
            return False
    return True


def show(state):
    bot, top = state
    C = Counter()
    for c in top:
        C[c] += 1
    for k, v in bot.items():
        for c in v:
            C[c] += 1
    assert C['A'] == 4
    assert C['B'] == 4
    assert C['C'] == 4
    assert C['D'] == 4
    assert C['E'] == 11
    assert top[2] == 'E'
    assert top[4] == 'E'
    assert top[6] == 'E'
    assert top[8] == 'E'


DP = {}


def f(state):
    # given a state, what is the cost to get to "done"?
    show(state)
    # move top -> L or R
    # move L or R ->
    # always move to destination ASAP
    bot, top = state
    key = (tuple((k, tuple(v)) for k, v in bot.items()), tuple(top))
    if done(state):
        return 0
    if key in DP:
        return DP[key]
    # move to dest if possible
    for i, c in enumerate(top):
        if c in bot and can_move_to(c, bot[c]):
            if clear_path(c, i, top):
                di = dest_idx(bot[c])
                assert di is not None
                dist = di + 1 + abs(bot_idx(c)-i)
                cost = COST[c] * dist
                new_top = list(top)
                new_top[i] = 'E'
                top[i] = 'E'
                new_bot = deepcopy(bot)
                new_bot[c][di] = c
                #print(f'Moved top={i} c={c} dest={di}')
                return cost + f((new_bot, new_top))

    ans = int(1e9)
    for k, col in bot.items():
        if not can_move_from(k, col):
            continue
        ki = top_idx(col)
        if ki is None:
            continue
        c = col[ki]
        for to_ in range(len(top)):
            if to_ in [2, 4, 6, 8]:
                continue
            if top[to_] != 'E':
                continue
            if clear_path(k, to_, top):
                dist = ki + 1 + abs(to_ - bot_idx(k))
                new_top = list(top)
                assert new_top[to_] == 'E'
                new_top[to_] = c
                new_bot = deepcopy(bot)
                assert new_bot[k][ki] == c
                new_bot[k][ki] = 'E'
                #print(f'Moved col={k} idx={ki} c={c} to {to_}')
                ans = min(ans, COST[c]*dist + f((new_bot, new_top)))
    DP[key] = ans
    #print(len(DP), ans)
    return ans


print(f(start))
