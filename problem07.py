from math import sqrt
def isprime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True

def iter_primes(n):
    i = 1
    while n > 0:
        if isprime(i):
            yield(i)
            n -= 1
        i += 1 

for p in iter_primes(10001):
    print p
