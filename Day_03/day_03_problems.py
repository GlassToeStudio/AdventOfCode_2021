"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to
produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers
which, when decoded properly, can tell you many useful things about the
conditions of the submarine. The first parameter to check is the power
consumption.

You need to use the binary numbers in the diagnostic report to generate two new
binary numbers (called the gamma rate and the epsilon rate). The power
consumption can then be found by multiplying the gamma rate by the epsilon
rate.

Each bit in the gamma rate can be determined by finding the most common bit in
the corresponding position of all numbers in the diagnostic report. For
example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven
1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the
second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0,
respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.
The epsilon rate is calculated in a similar way; rather than use the most
common bit, the least common bit from each position is used. So, the epsilon
rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon
rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate
and epsilon rate, then multiply them together. What is the power consumption
of the submarine? (Be sure to represent your answer in decimal, not binary.)


--- Part Two ---
Next, you should verify the life support rating, which can be determined by
multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that
can be found in your diagnostic report - finding them is the tricky part. Both
values are located using a similar process that involves filtering out values
until only one remains. Before searching for either rating value, start with
the full list of binary numbers from your diagnostic report and consider just
the first bit of those numbers. Then:


Keep only numbers selected by the bit criteria for the type of rating value for
which you are searching. Discard numbers which do not match the bit criteria.

If you only have one number left, stop; this is the rating value for which you
are searching.

Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in
the current bit position, and keep only numbers with that bit in that
position. If 0 and 1 are equally common, keep values with a 1 in the position
being considered.

To find CO2 scrubber rating, determine the least common value (0 or 1) in the
current bit position, and keep only numbers with that bit in that position. If
0 and 1 are equally common, keep values with a 0 in the position being
considered.


For example, to determine the oxygen generator rating value using the same
example diagnostic report from above:


Start with all 12 numbers and consider only the first bit of each number. There
are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in
the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.

Then, consider the second bit of the 7 remaining numbers: there are more 0 bits
(4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second
position: 10110, 10111, 10101, and 10000.

In the third position, three of the four numbers have a 1, so keep those three:
10110, 10111, and 10101.

In the fourth position, two of the three numbers have a 1, so keep those two:
10110 and 10111.

In the fifth position, there are an equal number of 0 bits and 1 bits (one
each). So, to find the oxygen generator rating, keep the number with a 1 in
that position: 10111.

As there is only one number left, stop; the oxygen generator rating is 10111,
or 23 in decimal.


Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number.
There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a
0 in the first position: 00100, 01111, 00111, 00010, and 01010.

Then, consider the second bit of the 5 remaining numbers: there are fewer 1
bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second
position: 01111 and 01010.

In the third position, there are an equal number of 0 bits and 1 bits (one
each). So, to find the CO2 scrubber rating, keep the number with a 0 in that
position: 01010.

As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10
in decimal.


Finally, to find the life support rating, multiply the oxygen generator rating
(23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen
generator rating and CO2 scrubber rating, then multiply them together. What is
the life support rating of the submarine? (Be sure to represent your answer in
decimal, not binary.)
"""


from io import TextIOWrapper


def format_data(data: TextIOWrapper) -> list[str]:
    """Return a list of ints from the given text."

    Args:
        data (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [x.strip() for x in data.readlines()]


def count_most_common_bit_at_index(data: list[str], i: int) -> int:
    """Given a list[str], data,  and index i, determine the most
    common bit (0 or 1) at index for each item in the list. If 
    there are an equal number of 0s and 1s, return 1.

    Args:
        data (list[str]): list of binary numbers represented as str
        i (int): index of bit to check

    Returns:
        int: most common bit at index i, (0 or 1)
    """

    if sum(int(x[i]) for x in data) >= len(data)/2:
        return '1'

    return '0'


def calc_power_consumption(data: list[str]) -> int:
    """Given a list of binary numbers represented as str,
    calculate the most common digit, and least common,
    digit at every index for each binary number.\n 
    Let gamma equal a new binary number comprised of most common digits
    Let epsilon equal a new bindary number for least common digit.\n
    Return the product of the two as an int.

    Args:
        data (list[str]): list of binary numbers represented as str

    Returns:
        int: product of gamma and epsilon
    """

    gamma = ''
    for i in range(len(data[0])):
        gamma += (count_most_common_bit_at_index(data, i))

    mask = int(('1' * len(gamma)), 2)
    gamma = int(gamma, 2)
    epsilon = ~gamma & mask

    return gamma * epsilon


def cal_oxygen_rating(data: list[str]) -> int:
    """Given a list of binary numbers represented as str,
    create two new copys of the list.
    Calculate the most common digit, and least common,
    digit at every index for each binary number in the new lists.\n

    For each iteration, remove any number from the first list that
    does not have the same digit as the common digit, at the specified index.
    Remove any number from the second list that does not have the
    least common digit, at the specified index.\n

    Recalculate the most and least common digits based on the modified lists.\n

    Let oxygen equal the final number in the fist list.
    Let co2 equal the final number in the second list.\n

    Return the product of the two as an int.

    Args:
        data (list[str]): list of binary numbers represented as str

    Returns:
        int: prodcut of oxygen and co2
    """

    oxy = list(data)
    co2 = list(data)
    for i in range(len(data[0])):
        oxy_val = count_most_common_bit_at_index(oxy, i)
        co2_val = count_most_common_bit_at_index(co2, i)

        for bin_num in data:
            # very similar but differnt methods
            if bin_num in oxy and len(oxy) > 1:
                if bin_num[i] != oxy_val and i != len(bin_num)-1:
                    oxy.remove(bin_num)
                elif bin_num[i] == '0' and i == len(bin_num) - 1:
                    oxy.remove(bin_num)

            if bin_num in co2 and len(co2) > 1:
                if bin_num[i] == co2_val and i != len(bin_num)-1:
                    co2.remove(bin_num)
                elif bin_num[i] == '1' and i == len(bin_num) - 1:
                    co2.remove(bin_num)

    oxy = int(''.join(oxy), 2)
    co2 = int(''.join(co2), 2)

    return oxy * co2


if __name__ == '__main__':
    with open('Day_03/input.txt', 'r') as in_file:
        data = format_data(in_file)
        print(f'Part 1: {calc_power_consumption(data)}')
        print(f'Part 2: {cal_oxygen_rating(data)}')

# Part 1: 1997414
# Part 2: 1032597
