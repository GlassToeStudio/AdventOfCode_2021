"""
--- Day 10: Syntax Scoring ---
You ask the submarine to determine the best route out of the deep-sea cave, but
it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the
navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks.
There are one or more chunks on each line, and chunks contain zero or more
other chunks. Adjacent chunks are not separated by any delimiter; if one chunk
stops, the next chunk (if any) can immediately start. Every chunk must open
and close with one of four legal pairs of matching characters:


If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More complex
but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and
even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the
corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that
is, where the characters it opens and closes with do not form one of the four
legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and
<([]){()}[{}]). Such a chunk can appear anywhere within a line, and its
presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]

Some of the lines aren't corrupted, just incomplete; you can ignore these lines
for now. The remaining five lines are corrupted:


{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

Stop at the first incorrect closing character on each corrupted line.
Did you know that syntax checkers actually have contests to see who can get the
high score for syntax errors in a file? It's true! To calculate the syntax
error score for a line, take the first illegal character on the line and look
it up in the following table:


): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal
] was found once (57 points), an illegal } was found once (1197 points), and
an illegal > was found once (25137 points). So, the total syntax error score
for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation
subsystem. What is the total syntax error score for those errors?



--- Part Two ---
Now, discard the corrupted lines.  The remaining lines are incomplete.
Incomplete lines don't have any incorrect characters - instead, they're missing
some closing characters at the end of the line. To repair the navigation
subsystem, you just need to figure out the sequence of closing characters that
complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in
the correct order so that only legal pairs are formed and all chunks end up
closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.

Did you know that autocomplete tools also have contests? It's true! The score
is determined by considering the completion string character-by-character.
Start with a total score of 0. Then, for each character, multiply the total
score by 5 and then increase the total score by the point value given for the
character in the following table:


): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.

So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a
new total score of 2.

Multiply the total score by 5 to get 10, then add the value of ) (1) to get a
new total score of 11.

Multiply the total score by 5 to get 55, then add the value of } (3) to get a
new total score of 58.

Multiply the total score by 5 to get 290, then add the value of > (4) to get a
new total score of 294.


The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.

Autocomplete tools are an odd bunch: the winner is found by sorting all of the
scores and then taking the middle score. (There will always be an odd number
of scores to consider.) In this example, the middle score is 288957 because
there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion
strings, and sort the scores. What is the middle score?

"""


import sys
import time
from io import TextIOWrapper
from os import system

from colors import BLACK_BG, GREEN, RED, RESET, UP, WHITE_BG, YELLOW


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [x.strip() for x in in_file.readlines()]


def find_corrupt_and_incomplete_line_scores(navigation_subsystem: list[list[str]]) -> tuple[int, int]:
    """For each line of sequences in the given navigation subsystem
    Find every 'corrupt chunk' which means to find the first incorrect
    closing bracket. Find just the first incorrect closing bracket
    then stop for that line. Each closing bracket has a score.
    Add the sum of scores for the first incorrect closing bracket
    for each line.

    For each line in the given navigation subsystem, that is not
    corrupt, search any incomplete lines to find the remaining
    required closing brackets that would complete the line.
    Each type of bracket has a score associated with it. Find
    the score of each incomplete line. Return the middle score.

    Args:
        navigation_subsystem (list[list[str]]):lines to parse

    Returns:
        tuple[int,int]: score for corrupt, median score for incomplete
    """

    chunk_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    point_dict_corrupt = {")": 3, "]": 57, "}": 1197, ">": 25137}
    point_dict_incomplete = {")": 1, "]": 2, "}": 3, ">": 4}

    points = 0
    scores = []
    finsihing_sequence = []
    for line in navigation_subsystem:
        chunks_open = []
        p_line = line  # VIS: This is only for viualization!
        i = 0  # VIS: This is only for viualization!
        for character in line:

            # Opening bracket found, add to the end of list
            if character in chunk_pairs:
                chunks_open.append(character)
                sys.stdout.write(f"{UP(1)}")  # VIS: This is only for viualization!
                print(f"{GREEN}{p_line[0:i]}{WHITE_BG}{p_line[i]}{RESET}{p_line[i+1:]}")  # VIS: This is only for viualization!
                i += 1  # VIS: This is only for viualization!
                time.sleep(0.001)  # VIS: This is only for viualization!
                continue

            # Matching closing bracket found, remove opening bracket from end of list.
            if character == chunk_pairs[chunks_open[-1]]:
                chunks_open.pop()
                sys.stdout.write(f"{UP(1)}")  # VIS: This is only for viualization!
                print(f'{f"{GREEN}{p_line[0:i]}{BLACK_BG}{p_line[i]}{RESET}{p_line[i+1:]}":120}')  # VIS: This is only for viualization!
                i += 1  # VIS: This is only for viualization!
                continue

            # we failed to complete a bracket: we have a corrupt line.
            # Calculate the points for the corrupt line and reset
            # the chunks open. Break and go to next line.
            points += point_dict_corrupt[character]
            sys.stdout.write(f"{UP(1)}")  # VIS: This is only for viualization!
            print(f'{f"{GREEN}{p_line[0:i]}{BLACK_BG}{RED}{p_line[i]}{RESET}{p_line[i+1:]}":132} : {YELLOW}{chunk_pairs[chunks_open[-1]]:10}{RESET}')  # VIS: This is only for viualization!
            print()  # VIS: This is only for viualization!
            chunks_open = None
            break

        # We have and incomplete line; chunks left open.
        # Find the required closing chunks and add the
        # sequence to the list.
        if chunks_open:
            sys.stdout.write(f"{UP(1)}")  # VIS: This is only for viualization!
            print(f'{f"{GREEN}{p_line[0:i]}{RESET}":120} : {YELLOW}{"".join([chunk_pairs[x] for x in reversed(chunks_open)]):10}{RESET}')  # VIS: This is only for viualization!
            print()  # VIS: This is only for viualization!
            finsihing_sequence.append([chunk_pairs[x] for x in reversed(chunks_open)])

    # Calculate the median score for incomplete lines
    for sequence in finsihing_sequence:
        score = 0
        for character in sequence:
            score = score * 5 + point_dict_incomplete[character]
        scores.append(score)
    scores.sort()
    return points, scores[len(scores) // 2]


if __name__ == "__main__":
    with open("Day_10/input.txt", "r", encoding="utf-8") as f:
        data = format_data(f)
    _ = system("cls")  # VIS: This is only for viualization!
    p1, p2 = find_corrupt_and_incomplete_line_scores(data)
    print(f"# Part 1: {p1:10}")
    print(f"# Part 2: {p2:10}")

# Part 1:     168417
# Part 2: 2802519786
