from lib import sieve
# divisors given prime factorisation
# d = product over primes: (exponent + 1)

s = sieve()

triangle = 1
i = 2
while s.num_divisors(triangle) < 500:
    triangle += i
    i += 1
print triangle
