from math import sqrt

n = 600851475143
test = 13195

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True

def max_factor(n):
    for i in reversed(range(1, int(sqrt(n)))):
        if (not n % i) and is_prime(i):
            return i

print [ "%s: %s" % (x, max_factor(x)) for x in [n, test]]
