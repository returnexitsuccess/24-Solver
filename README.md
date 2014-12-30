24-Solver
=========

Written in Python 2.7

Finds arithmetic operations to be combined with four given numbers to make the total 24.

For example if given the numbers 2 6 7 8, a valid solution would be (((2 + 7) - 6) * 8) because it equals 24. Valid operations are +,-,*,/

Solutions are represented using three different lists, the order of operations, the operations, and the numbers. For example the solution to 2 6 7 8 above would look like this if outputted from 24.py:

[0, 1, 2]

['+', '-', *]

[2, 7, 6, 8]

The first line means that the order of operations or order of parentheses is the first, then the second, then the third. The second and third line then give which operations and the order to put the numbers. For example if you saw,

[1, 0, 2]

['-', '*', '*']

[1, 2, 3, 4],

then that would correspond with the expression ((1 - (2 * 3)) * 4), where the middle operation, then the left operation, then the right operation is performed because of the 0 in the middle, 1 on the left, and 2 on the right.


Once a single solution is found the program terminates and does not attempt to find further solutions.
