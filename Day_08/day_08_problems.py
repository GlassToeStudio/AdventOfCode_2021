"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave
mouth, collapsing it. Sensors indicate another exit to this cave at a much
greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that
the four-digit seven-segment displays in your submarine are malfunctioning;
they must have been damaged during the escape. You'll be in a lot of trouble
without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of
seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

So, to render a 1, only segments c and f would be turned on; the rest would be
off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up
on each display. The submarine is still trying to display numbers by producing
output on signal wires a through g, but those wires are connected to segments
randomly. Worse, the wire/segment connections are mixed up separately for each
four-digit display! (All of the digits within a display use the same
connections, though.)

So, you might know that only signal wires b and g are turned on, but that
doesn't mean segments b and g are turned on: the only digit that uses two
segments is 1, so it must mean segments c and f are meant to be on. With just
that information, you still can't tell which wire (b/g) goes to which segment
(c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of
all ten unique signal patterns you see, and then write down a single four
digit output value (your puzzle input). Using the signal patterns, you should
be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all
be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally
the four digit output value. Within an entry, the same wire/segment
connections are used (but you don't know what the connections actually are).
The unique signal patterns correspond to the ten different ways the submarine
tries to render a digit using the current wire/segment connections. Because 7
is the only digit that uses three segments, dab in the above example means
that to render a 7, signal lines d, a, and b are on. Because 4 is the only
digit that uses four segments, eafb means that to render a 4, signal lines e,
a, f, and b are on.

Using this information, you should be able to work out which combination of
signal wires corresponds to each of the ten digits. Then, you can decode the
four digit output value. Unfortunately, in the above example, all of the
digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are
more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
should be able to tell which combinations of signals correspond to those
digits. Counting only digits in the output values (the part after | on each
line), in the above example, there are 26 instances of digits that use a
unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?


--- Part Two ---
Through a little deduction, you should now be able to determine the remaining
digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only
make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1

Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3

Therefore, the output value for this entry is 5353.
Following this same process for each entry in the second, larger example above,
the output value of each entry can be determined:


fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.
For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output
values?
"""


from io import TextIOWrapper

UNIQUES: dict[int, str] = {2: "1", 3: "7", 4: "4", 7: "8"}
"""Dictionary of {length : digit} for the 4 unique digits"""

CYPHER: dict[tuple[int, int, int], str] = {(2, 3, 6): "0", (1, 2, 5): "2", (2, 3, 5): "3", (1, 3, 5): "5", (1, 3, 6): "6", (2, 4, 6): "9"}
"""Dictionary of {tuple : digit} for the remaining 6 values. The tuple is 1 & digit, 4 & digit, len(digit)) """


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return in_file.readlines()


def find_digit(signals: list[str], length: int) -> str:
    """Find the signal in the list that has the same length
    as the passed in value.

    Only useful for 1, 4, 7, 8 which have unique lengths.

    Args:
        signals (list[str]): list of signals in which to search
        length (int): length of the digit to find.

    Returns:
        int: the found sequence representing a digit.
    """

    return [x for x in signals if len(x) == length][0]


def like_digit(find: str, digit: str) -> int:
    """Return the number of similarities between the find
    string and the digit string.

    Args:
        find (str): The sequence representing the number to find
        digit (str): The sequence representing where to search.

    Returns:
        int: Number of similarities between find and digit.
    """

    return sum(1 for n in digit if n in find)


def part1(pattern_output: list[str]) -> int:
    """Find the sum of the number of digits with a unique length.
    i.e. How many 1, 4, 7, and 8 are there.

    Search in only the digital output value of the data.
    (unique signal pattern | digital output value)

    Args:
        pattern_output (list[str]): List of signals and digits.

    Returns:
        int: total occurrences of 1, 4, 7, 8
    """

    # Get only the right half, digital values, from the input.
    digital = [z.strip() for x in pattern_output for y in x.split(" | ")[1::2] for z in y.split()]
    return sum(1 for x in digital if len(x) in UNIQUES)


def part2(pattern_output: list[str]) -> int:
    """Decipher the digital output values of the given data.
    (unique signal pattern | digital output value)

    Each output represents a 4 digit number. Sum the total
    of all digital outputs.

    Args:
        pattern_output (list[str]): List of signals and digits.

    Returns:
        int: Sum of all output values
    """

    total = 0
    for line in pattern_output:
        answers = [None] * 4
        _s, _d = line.strip().split(" | ")
        signal = _s.split()
        digital = _d.split()

        # We can use 1 and 4 to decipher the remaining numbers.
        one = find_digit(signal, 2)
        four = find_digit(signal, 4)

        # Go ahead and check for the numbers we can find just
        # by length (1, 4, 7, 8)
        for i, digit in enumerate(digital):
            if len(digit) in UNIQUES:
                answers[i] = UNIQUES[len(digit)]

        # If we have not already found all 4 digital values,
        # decipher each remaining value by comparing it to 1
        # and 4. Every remaining number (0, 2, 3, 5, 6, 9) has
        # a unique similarity to 1 and 4 along with its length.
        for i, answer in enumerate(answers):
            if answer is None:
                answers[i] = CYPHER[(like_digit(one, digital[i]), like_digit(four, digital[i]), len(digital[i]))]
        total += int("".join(answers))
    return total


if __name__ == "__main__":
    with open("Day_08/input.txt", "r", encoding="utf-8") as f:
        data = format_data(f)
    print(f"# Part 1: {part1(data):6}")
    print(f"# Part 2: {part2(data):6}")


# Part 1:    318
# Part 2: 996280
