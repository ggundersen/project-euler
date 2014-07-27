"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?

Solution:
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    result = 0
    gen = g.gen_sieve_of_eratosthenes()
    for i in range(10001):
        p = gen.next()
        result = p
    return result