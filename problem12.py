

# the ith triangular number
# n = (i*(i + 1)) / 2

# divisors given prime factorisation
# d = product over primes: (exponent + 1)

# Hmmm....

def num_factors(n):
    return len([i for i in range(1, n/2+1) if not n % i])


i = 1
triangle = 1

while num_factors(triangle) <= 100:
    triangle += i
    print triangle
    i += 1

print triangle
