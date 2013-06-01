from lib import sieve
print sum(sieve().prime_generator( lambda i, p: i < int(2e6)))
