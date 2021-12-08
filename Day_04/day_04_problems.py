"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean,
already so deep that you can't see any sunlight. What you can see, however, is
a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards on
which it appears. (Numbers may not appear on all boards.) If all numbers in
any row or any column of a board are marked, that board wins. (Diagonals don't
count.)

The submarine has a bingo subsystem to help passengers (currently, you and the
giant squid) pass the time. It automatically generates a random order in which
to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no
winners, but the boards are marked as follows (shown here adjacent to each
other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are
still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:
22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or
column of marked numbers (in this case, the entire top row is marked: 14 21 17
24  4).

The score of the winning board can now be calculated. Start by finding the sum
of all unmarked numbers on that board; in this case, the sum is 188. Then,
multiply that sum by the number that was just called when the board won, 24,
to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win
first. What will your final score be if you choose that board?


--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant
squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure
out which board will win last and choose that one. That way, no matter which
boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after
13 is eventually called and its middle column is completely marked. If you
were to keep playing until this point, the second board would have a sum of
unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score
be?
"""

import sys
import time
from io import TextIOWrapper
from os import system

#                                                               # VIS: This is only for makeing an image!
from colors import BLACK_BR, BLINK_OFF, END, HOME, INV, RED

#                                                               # VIS: This is only for makeing an image!
NEW_LINE = "\n"
TAB = "\t"
SQUID = (" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
         rf"{TAB*4}                         {RED}                       ___                              {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}                    .-'   `'.                           {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}                   /         \                          {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}                   |         ;                          {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}       ______     _____  {RED}                   |         |           ___.--,        {BLACK_BR}    _____      ____   {NEW_LINE}"
         rf"{TAB*4}      (_   _ \   (_   _) {RED}          _.._     |0) ~ (0) |    _.---'`__.-( (_.      {BLACK_BR}   / ___ \    / __ \  {NEW_LINE}"
         rf"{TAB*4}        ) (_) )    | |   {RED}   __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `\"\"`    {BLACK_BR}  / /   \_)  / /  \ \ {NEW_LINE}"
         rf"{TAB*4}        \   _/     | |   {RED}  ( ,.--'`   ',__ /./;   ;, '.__.'`    __               {BLACK_BR} ( (  ____  ( ()  () ){NEW_LINE}"
         rf"{TAB*4}        /  _ \     | |   {RED}  _`) )  .---.__.' / |   |\   \__..--\"\"  \"\"\"--.,_  {BLACK_BR} ( ( (__  ) ( ()  () ){NEW_LINE}"
         rf"{TAB*4}       _) (_) )   _| |__ {RED} `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'{BLACK_BR}  \ \__/ /   \ \__/ / {NEW_LINE}"
         rf"{TAB*4}      (______/   /_____( {RED}       | |  .' _.-' |  |  \  \  '.               `~---` {BLACK_BR}   \____/     \____/  {NEW_LINE}"
         rf"{TAB*4}                         {RED}        \ \/ .'     \  \   '. '-._)                     {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}         \/ /        \  \    `=.__`~-.                  {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}         / /\         `) )    / / `\"\".`\              {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}   , _.-'.'\ \        / /    ( (     / /                {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}    `--~`   ) )    .-'.'      '.'.  | (                 {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}           (/`    ( (`          ) )  '-;                {BLACK_BR}                      {NEW_LINE}"
         rf"{TAB*4}                         {RED}            `      '-;         (-'                      {BLACK_BR}                      {NEW_LINE}"
         " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
         )

BALL = "🔴"                                                     # VIS: This is only for makeing an image!
SPECIAL_BALL = "🔵"                                             # VIS: This is only for makeing an image!


def change_winning_baord(board: list[int]) -> list[int]:        # VIS: This is only for makeing an image!
    """Change the colors of the marked spots on in the board.

    Args:
        board (list[int]): initial marked board

    Returns:
        list[int]: modified marked board
    """

    return [SPECIAL_BALL if x == BALL else x for x in board]


def print_one_board(board: list[int]) -> None:                  # VIS: This is only for makeing an image!
    """Print the board

    Args:
        board (list[int]): the board to print
    """

    print()
    for i in range(0, 25, 5):
        for j in range(5):
            if board[i+j] == BALL:
                print(f"{BALL}", end=' ')
            else:
                print(f"{SPECIAL_BALL}", end=' ')
        print('\n')


def print_all_boards(boards: list[list[int]]) -> None:          # VIS: This is only for makeing an image!
    """Print all boards to the terminal.

    Args:
        boards (list[list[int]]): The boards to print.
    """

    sys.stdout.write(HOME)
    output = '\n\n'
    for boards_m in range(0, 100, 10):
        for rows_k in range(0, 25, 5):
            for board_j in range(boards_m, 10+boards_m):
                for ball_i in range(rows_k, 5+rows_k):
                    if boards[board_j][ball_i] == BALL:
                        output += (f" {BALL}")
                    elif boards[board_j][ball_i] == SPECIAL_BALL:
                        output += (f" {SPECIAL_BALL}")
                    else:
                        output += (f"{boards[board_j][ball_i]:3}")
                output += " "
            output += "\n"
        output += "\n"
    output += SQUID

    sys.stdout.write(output)


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return list(in_file.readlines())


def parse_balls(ball_data: list[str]) -> list[int]:
    """Return a list of int representing each ball
    drawn for the bingo game.

    Args:
        ball_data (list[str]): contains the unparsed ball data

    Returns:
        list[int]: values of balls drawn
    """

    return [int(x) for x in ball_data[0].split(",")]


def parse_boards(board_data: list[str]) -> list[list[int]]:
    """Return a list containing the data for each bingo
    board. Each board is a list withing the returned list.

    Args:
        board_data (list[str]): unparsed board data

    Returns:
        list[list[int]]: Each board as entry in a list
    """

    boards = []
    for i in range(0, len(board_data)-1, 6):
        boards.append([int(y) for x in board_data[i:i + 5] for y in x.split()])

    return boards


def place_ball(ball: int, board: list[int]) -> list[int]:
    """Checks if the board contains the passed in ball value.
    If so, replace the value on the board with a ⚫ to mark it.
    Return the modified board.

    Args:
        ball (int): Value of the current ball
        board (list[int]): Current board

    Returns:
        list[int]: Modified board denoting marked values
    """

    return [BALL if x == ball else x for x in board]                # VIS: This is only for makeing an image! (BALL could be anything else.)


def check_rows(board: list[int]) -> bool:
    """Checks each row in the board to see if every
    entry in that row is marked. If so, return true
    else false.

    Args:
        board (list[int]): Current board

    Returns:
        bool: True if winning board else false
    """

    for i in range(0, 25, 5):
        total = sum(1 for x in board[i: i + 5] if x == BALL) == 5
        if total:
            return True
    return False


def check_columns(board: list[int]) -> bool:
    """Checks each column in the board to see if every
    entry in that column is marked. If so, return true
    else false.

    Args:
        board (list[int]): Current board

    Returns:
        bool: True if winning board else false
    """

    for i in range(0, 5):
        total = sum(1 for j in range(0, 25, 5) if board[i + j] == BALL) == 5
        if total:
            return True
    return False


def calc_solution(winning_ball: int, winning_board: list[int]) -> int:
    """Sum all remaining unmarked values on the board.
    Return the product of the sum and the value of the ball.

    Args:
        winning_ball (int): Value of winning ball
        winning_board (list[int]): Winning board

    Returns:
        int: final value for winning
    """

    return sum(x for x in winning_board if (x != BALL and x != SPECIAL_BALL)) * winning_ball     # VIS: This is only for makeing an image! BALL should be 0


def main(input_data: list[str]) -> tuple[int, int]:
    """Run the bingo simulation until the last winning
    board is found. Return the solution for the first
    and last winning boards/

    Args:
        input_data (list[str]): input from file

    Returns:
        tuple[int, int]: winning values for 1st and last winners
    """
    first_winner = False                                            # VIS: This is only for makeing an image!
    winners = []
    w_ball = []
    balls = parse_balls(input_data)
    boards = parse_boards(input_data[2:])
    for ball in balls:
        for j, _ in enumerate(boards):
            if j in winners:
                continue
            boards[j] = place_ball(ball, boards[j])
            if check_rows(boards[j]) or check_columns(boards[j]):
                if not first_winner:                                # VIS: This is only for makeing an image!
                    boards[j] = change_winning_baord(boards[j])     # VIS: This is only for makeing an image!
                    first_winner = True                             # VIS: This is only for makeing an image!
                winners.append(j)
                w_ball.append(ball)
                continue
        time.sleep(.05)
        print_all_boards(boards)                                # VIS: This is only for makeing an image!
    # print_one_board(boards[winners[0]])
    boards[winners[-1]] = change_winning_baord(boards[winners[-1]])
    print_all_boards(boards)                                        # VIS: This is only for makeing an image!
    return (calc_solution(w_ball[0], boards[winners[0]]),
            calc_solution(w_ball[-1], boards[winners[-1]]))


if __name__ == "__main__":
    with open("Day_04/input.txt", 'r', encoding='utf-8') as f:
        data = format_data(f)
    sys.stdout.write(HOME)
    _ = system('cls')                                               # VIS: This is only for makeing an image!
    sys.stdout.write(f"{INV}{BLINK_OFF}{BLACK_BR}")                 # VIS: This is only for makeing an image!
    p1, p2 = main(data)
    print(f"Part 1: {p1:5}")
    print(f"Part 2: {p2:5}\n")
    sys.stdout.write(END)                                           # VIS: This is only for makeing an image!
time.sleep(1)                                                       # VIS: This is only for makeing an image!
sys.stdout.flush()                                                  # VIS: This is only for makeing an image!

# Part 1: 23177
# Part 2: 6804
