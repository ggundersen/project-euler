"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
----------------------------------------------------------------------------"""


def main():
    return sum([int(i) for i in str(2**1000)])
