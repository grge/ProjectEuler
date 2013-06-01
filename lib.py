import os
from math import sqrt
from operator import mul
from itertools import groupby
from time import time

class Problem(object):
    known_answer = None
    data_path = os.path.join(os.path.dirname(__file__), 'data')

    def __init__(self, data=None):
        if data:
            for filename in data:
                self.data[filename] = open(os.path.join(self.data_path, filename), 'r').read()

    def solve(self):
        pass

    def test():
        t1 = time()
        r = self.solve() 
        t2 = time()
        return (r, t2-t1, r == known_answer and known_answer)
    
def product(list):
    return reduce(mul, list)

# returns i if n is the ith triangular number or False
def is_triangular(n):
    triangular_root = (sqrt(8 * n + 1) - 1)/2
    if int(triangular_root) == triangular_root:
        return int(triangular_root)
    else:
        return False

def fibs_up_to(n):
    (a, b) = (1, 2)
    while a < n:
        yield a
        (a, b) = (b, a + b)

class sieve(object):
    def __init__(self, n=1000):
        self.sieve = [False, False, True, True, False, True]
        self.extend(n)

    @property
    def size(self):
        return len(self.sieve)

    def extend(self, n):  
        if n <= self.size:
            return
        self.sieve.extend([True] * (n - self.size + 1))
        for i in range(1, int(n/2)):
            if self.sieve[i]:
                for j in range(i**2, n+1, i):
                    self.sieve[j] = False

    def is_prime(self, n):
        if n >= self.size - 1:
            self.extend(n*2)
        return self.sieve[n]

    # generates primes until the predicate returns False
    # the predicate takes: 
    #       i = the current integer
    #       p = the prime counting function p(i)
    def prime_generator(self, predicate):
        (i, p) = (1,0)
        while predicate(i, p):
            if self.is_prime(i): 
                yield i
                p += 1
            i += 1

    # generates the first n prime numbers
    def n_primes(self, n):
        pred = lambda i, p : True if p < n else False
        for prime in self.prime_generator(pred): yield prime

    def nth_prime(self, n):
        item = 2
        for item in self.n_primes: pass
        return item

    # sieve.factors(12) -> [2, 2, 3]
    def factors(self, n):
        for i in range(1, int(sqrt(n)) + 1):
            if (not n % i) and self.is_prime(i):
                return [i] + self.factors(n / i)
        return [n]

    # sieve.group_factors(12) -> [(2,2), (3,1)]
    def group_factors(self, n):
        for p, group in groupby(self.factors(n)):
            yield p, len(list(group))

    def num_divisors(self, n):
        return product([n + 1 for p, n in self.group_factors(n)])

class memoize:
    def __init__(self, f):
        self.f = f
        self.mem = {}
    def __call__(self, *args, **kwargs):
        if (args, str(kwargs)) in self.mem:
            return self.mem[args, str(kwargs)]
        else:
            tmp = self.f(*args, **kwargs)
            self.mem[args, str(kwargs)] = tmp
            return tmp

