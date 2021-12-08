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



<details>
<summary><b>Day 4: Giant Squid</b></summary>
<p>
Play BINGO!
From list of balls chosen, and a set of many bingo boards,
find the bingo boards that are winners.

```
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
```

### Part 1:
Find the first winning bingo board to beat the giant squid.

<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2021/blob/master/Day_04/Giant_Squid_Bingo.gif" width="85%" height="85%"
</p>

### Part 2:
Find the last winning bingo board to insure the giant squid wins.

</p>
</details>



<details>
<summary><b>Day 5: Hydrothermal Venture</b></summary>
<p>
Given a set of line segments as two points, graph each line segment.

```
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

### Part 1:
Graph each point the line segment covers. Find all areas that have at least 1 overlap. Only consider horizontal and vertical lines.

### Part 2:
Graph each point the line segment covers. Find all areas that have at least 1 overlap. Consider horizontal, vertical lines and diagnoanl lines..

<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2021/blob/master/Day_05/day_05_vis_large.png" width="50%" height="50%"
</p>

</p>
</details>



<details>
<summary><b>Day 6: Lanternfish</b></summary>
<p>
Fish everywhere. Given a set of data: a list of numbers, each number represents how long until the fish reproduces. A fish reproduces once every 7 days. New born fish take 8 days for their first offspring. Find the number of fish after n days.

```
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```

### Part 1:
Find a way to simulate lanternfish. How many lanternfish would there be after
80 days?

### Part 2:
How many lanternfish would there be after 256 days?

</p>
</details>



<details>
<summary><b>Day 7: The Treachery of Whales</b></summary>
<p>
Overall description

```

```

### Part 1:
Part 1 description

### Part 2:
Part 2 description

</p>
</details>



<details>
<summary><b>Day 8: Seven Segment Search</b></summary>
<p>
Overall description

```

```

### Part 1:
Part 1 description

### Part 2:
Part 2 description

</p>
</details>