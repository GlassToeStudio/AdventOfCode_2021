# Advent Of Code 2021
Advent of Code 2021: https://adventofcode.com/2021

<details>
<summary><b>Day 1: Sonar Sweep</b></summary>
<p>
From a list of numbers (depths), count how many depths are greater than the previous depth.

```
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

### Part 1:
Count how many increases in depth there are. 

### Part 2:
Take the sum of every three consecutive depths and then count the increases in the sums.
</p>
</details>



<details>
<summary><b>Day 2: Dive!</b></summary>
<p>
From a list of directions and amounts (course), calculate the
depth and distance traveled.

```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

### Part 1:
Calculate the product of the final depth and distance.

### Part 2:
Calculate depth by using an aiming factor based on distance.
Calculate the product of the final depth and distance.
</p>
</details>



<details>
<summary><b>Day 3: Binary Diagnostic</b></summary>
<p>
From a list of binary numbers, perform some operations
to determine most common and least common bits at index.
These are used to create two new binary numbers.

```
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
```

### Part 1:
Construct a binary number based on the most common bit at 
index for each number in the list.
Construct a binary number based on the least common bit at 
index for each number in the list. (opposite of previous number)

FInd the product of those two numbers.

### Part 2:
This time you find the most common bit at index for a copy of the list of numbers, but remove any number that does not have that bit at that index. And the least common bit at index for a copy of the original list and
remove any numbers that do not have that bit at that index.

Keep doing that for the modified list until one number remains.

Get the product of the two final numbers.

</p>
</details>