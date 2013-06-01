from math import sqrt

from lib import sieve
n = 600851475143
test = 13195

s = sieve()
def max_factor(n):
    for i in reversed(range(1, int(sqrt(n)))):
        if (not n % i) and s.is_prime(i):
            return i

print [ "%s: %s" % (x, max_factor(x)) for x in [n, test]]
