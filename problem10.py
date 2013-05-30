from math import sqrt
def isprime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True

print sum([i for i in range(int(2e6)) if isprime(i)])
