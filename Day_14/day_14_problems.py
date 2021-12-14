"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your
submarine. The submarine has polymerization equipment that would produce
suitable materials to reinforce the submarine, and the nearby
volcanically-active caves should even have the necessary input elements in
sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer
formula; specifically, it offers a polymer template and a list of pair
insertion rules (your puzzle input). You just need to work out what polymer
would result after repeating the pair insertion process a few times.

For example:
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of the
process.

The following section defines the pair insertion rules. A rule like AB -> C
means that when elements A and B are immediately adjacent, element C should be
inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously
considers all three pairs:


The first pair (NN) matches the rule NN -> C, so element C is inserted between
the first N and the second N.

The second pair (NC) matches the rule NC -> B, so element B is inserted between
the N and the C.

The third pair (CB) matches the rule CB -> H, so element H is inserted between
the C and the B.


Note that these pairs overlap: the second element of one pair is the first
element of the next pair. Also, because all pairs are considered
simultaneously, inserted elements are not considered to be part of a pair
until the next step.

After the first step of this process, the polymer becomes NCNBCHB.
Here are the results of a few steps using the above rules:
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it
has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H
occurs 161 times, and N occurs 865 times; taking the quantity of the most
common element (B, 1749) and subtracting the quantity of the least common
element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity
of the most common element and subtract the quantity of the least common
element?


--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine.
You'll need to run more steps of the pair insertion process; a total of 40
steps should do it.

In the above example, the most common element is B (occurring 2192039569602
times) and the least common element is H (occurring 3849876073 times);
subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity
of the most common element and subtract the quantity of the least common
element?
"""


from collections import Counter
from io import TextIOWrapper


def format_data(in_file: TextIOWrapper) -> tuple[str, dict[str, str]]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
       tuple[str, dict[str, str]]: template, rules
    """

    lines = in_file.readlines()
    template = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        x, y = line.strip().split(" -> ")
        rules[x] = y

    return template, rules


def count_pairs(template: str, rules: dict[str, str], iterations: int) -> int:
    """Count each time a rule (pair) appears in the template. Then, for
    every iteration, keep track of how many times the pairs would appear
    in the template by checking what pairs are already being tracked. Add
    these pairs to the count. Once all the pairs are counted for every iteration,
    loop of the final count to count each letter in the pairs. Return
    The most common letter minus the least common letter.

    Args:
        template (str): initial string to count pairs
        rules (dict[str,str]): how to alter each pair
        iterations (int): number of iterations to count the pairs

    Returns:
        int: most common - least common letter.
    """

    pair_count = Counter()
    for i in range(len(template) - 1):
        pair_count[template[i: i + 2]] += 1

    for _ in range(iterations):
        temp_count = Counter()
        for pair in pair_count:
            temp_count[f"{pair[0]}{rules[pair]}"] += pair_count[pair]
            temp_count[f"{rules[pair]}{pair[1]}"] += pair_count[pair]
        pair_count = temp_count

    letter_count = Counter()
    for pair in pair_count:
        letter_count[pair[0]] += pair_count[pair]
    letter_count[template[-1]] += 1

    return most_minus_least(letter_count)


def most_minus_least(counts: Counter[str, int]) -> int:
    """From the given counter object, return the most
    common item - the least common item

    Args:
        counts (Counter[str, int]): a counter of letters, counts

    Returns:
        int: most common - least common letter in counts
    """

    order = counts.most_common()
    return order[0][1] - order[-1][1]


if __name__ == "__main__":
    with open("Day_14/input.txt", "r", encoding="utf-8") as f:
        polymer_template, insertion_rules = format_data(f)

    print(f"# Part 1: {count_pairs(polymer_template, insertion_rules, 10):13}")
    print(f"# Part 2: {count_pairs(polymer_template, insertion_rules, 40):13}")

# Part 1:          2745
# Part 2: 3420801168962
