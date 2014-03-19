"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-29

Problem:
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle        T_n = n*(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      P_n = n*(3n-1)/2    1, 5, 12, 22, 35, ...
Hexagonal       H_n = n*(2n-1)      1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

Solution:
1533776805
Behold, the power of hashing. Also, if a number is a hexagonal number, it is a
triangle number. We do not need to check both.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    pent, hexa, bound = {}, {}, 40755
    for i in range(1, 100000):
        p = g.get_pentagonal_number(i)
        h = g.get_hexagonal_number(i)
        pent[p] = p
        hexa[h] = h

    for p in pent:
        if hexa.get(p) and p > bound:
            return p