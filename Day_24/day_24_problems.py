"""


--- Day 24: Arithmetic Logic Unit ---
Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU).
Without the ability to perform basic arithmetic and logic functions, the
submarine can't produce cool patterns with its Christmas lights!

It also can't navigate. Or run the oxygen system.
Don't worry, though - you probably have enough oxygen left to give you enough
time to build a new ALU.

The ALU is a four-dimensional processing unit: it has integer variables w, x,
y, and z. These variables all start with the value 0. The ALU also supports
six instructions:


inp a - Read an input value and write it to variable a.
add a b - Add the value of a to the value of b, then store the result in
variable a.

mul a b - Multiply the value of a by the value of b, then store the result in
variable a.

div a b - Divide the value of a by the value of b, truncate the result to an
integer, then store the result in variable a. (Here, "truncate" means to round
the value toward zero.)

mod a b - Divide the value of a by the value of b, then store the remainder in
variable a. (This is also called the modulo operation.)

eql a b - If the value of a and b are equal, then store the value 1 in variable
a. Otherwise, store the value 0 in variable a.


In all of these instructions, a and b are placeholders; a will always be the
variable where the result of the operation is stored (one of w, x, y, or z),
while b can be either a variable or a number. Numbers can be positive or
negative, but will always be integers.

The ALU has no jump instructions; in an ALU program, every instruction is run
exactly once in order from top to bottom. The program halts after the last
instruction has finished executing.

(Program authors should be especially cautious; attempting to execute div with
b=0 or attempting to execute mod with a<0 or b<=0  will cause the program to
crash and might even damage the ALU. These operations are never intended in
any serious ALU program.)

For example, here is an ALU program which takes an input number, negates it,
and stores it in x:

inp x
mul x -1

Here is an ALU program which takes two input numbers, then sets z to 1 if the
second input number is three times larger than the first input number, or sets
z to 0 otherwise:

inp z
inp x
mul z 3
eql z x

Here is an ALU program which takes a non-negative integer as input, converts it
into binary, and stores the lowest (1's) bit in z, the second-lowest (2's) bit
in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit in w:

inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2

Once you have built a replacement ALU, you can install it in the submarine,
which will immediately resume what it was doing when the ALU failed:
validating the submarine's model number. To do this, the ALU will run the
MOdel Number Automatic Detector program (MONAD, your puzzle input).

Submarine model numbers are always fourteen-digit numbers consisting only of
digits 1 through 9. The digit 0 cannot appear in a model number.

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen
separate inp instructions, each expecting a single digit of the model number
in order of most to least significant. (So, to check the model number
13579246899999, you would give 1 to the first inp instruction, 3 to the second
inp instruction, 5 to the third inp instruction, and so on.) This means that
when operating MONAD, each input instruction should only ever be given an
integer value of at least 1 and at most 9.

Then, after MONAD has finished running all of its instructions, it will
indicate that the model number was valid by leaving a 0 in variable z.
However, if the model number was invalid, it will leave some other non-zero
value in z.

MONAD imposes additional, mysterious restrictions on model numbers, and legend
says the last copy of the MONAD documentation was eaten by a tanuki. You'll
need to figure out what MONAD does some other way.

To enable as many submarine features as possible, find the largest valid
fourteen-digit model number that contains no 0 digits. What is the largest
model number accepted by MONAD?


"""


import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from io import TextIOWrapper
from typing import (Any, Callable, Collection, DefaultDict, Dict, Generic,
                    Iterable, Iterator, List, Mapping, MutableSet, Sequence,
                    Tuple, TypeVar)


def format_data(in_file: TextIOWrapper) -> list[str]:
    """Return a list of str from the given text."

    Args:
        in_file (TextIOWrapper): text file

    Returns:
        list[str]: input data as list[str]
    """

    return [x.strip() for x in in_file.readlines()]


if __name__ == "__main__":
    with open("Day_24/input.txt", "r", encoding='utf-8') as f:
        data = format_data(f)
        print(data)


def lines(inp: str = None) -> List[str]:
    return (inp or sys.stdin.read()).splitlines()


if len(sys.argv) == 1:
    sys.stdin = open("Day_24/input.txt")

FS = sys.stdin.read()
secs = FS.split('inp w\n')[1:]
secs = [[s.split() for s in lines(sec)] for sec in secs]
N = len(secs)
assert N == 14

op_map = dict(zip('add mul div mod'.split(), '+ * // %'.split()))

generated_code = ''
for i, sec in enumerate(secs):
    opt = []
    for instr, x, y in sec:
        if instr == 'eql':
            opt.append(f'{x} = int({x} == {y})')
        else:
            opt.append(f'{x} {op_map[instr]}= {y}')

    generated_code += f'def f_{i}(w, z, x=0, y=0):\n'
    opt.append('return z')
    generated_code += '\n'.join('\t' + s for s in opt) + '\n\n'

generated_code += 'funs = [' + ', '.join(f'f_{i}' for i in range(14)) + ']'
exec(generated_code)

cache = [set() for _ in range(14)]


def run(sec_no: int, pz: int) -> int:
    if sec_no == N:  # or pz > 10 ** 7:
        return 0 if pz == 0 else -1

    if pz in cache[sec_no]:
        return -1

    for w in range(9, 0, -1):
        # for w in range(1, 10):
        nz = funs[sec_no](w, pz)
        r = run(sec_no + 1, nz)
        if r != -1:
            return r + w * 10 ** (N - sec_no - 1)

    cache[sec_no].add(pz)
    return -1


print(run(0, 0))
