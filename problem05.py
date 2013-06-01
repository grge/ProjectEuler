from itertools import groupby
from math import sqrt
from operator import mul
from lib import sieve

s = sieve()

f = [[(k, len(list(v))) for k, v in groupby(sorted(s.factors(n)))] for n in range(1, 20)]

new_factors = {k: 0 for k in range(1, 20)}
for n in range(1, 20):
    for k, v in groupby(sorted(s.factors(n))):
        power = len(list(v))
        if new_factors[k] < power:
            new_factors[k] = power

print(reduce(mul, [k**v for k, v in new_factors.iteritems()]))


