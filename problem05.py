from itertools import groupby
from math import sqrt
from operator import mul

def isprime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True

def factors(n):
    for i in range(1, int(sqrt(n) + 1)):
        if (not n % i) and isprime(i):
            return [i] + factors(n / i)
    return [n]

f = [[(k, len(list(v))) for k, v in groupby(sorted(factors(n)))] for n in range(1, 20)]

new_factors = {k: 0 for k in range(1, 20)}
for n in range(1, 20):
    for k, v in groupby(sorted(factors(n))):
        power = len(list(v))
        if new_factors[k] < power:
            new_factors[k] = power

print(reduce(mul, [k**v for k, v in new_factors.iteritems()]))


