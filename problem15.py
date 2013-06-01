# path is 20 units long and consists of 10 up and 10 across
# in any permutation
# = 10 choose 20
# = 20! / 10! * 10!

from lib import product
print product(range(1,21)) / (product(range(1,11)) * product(range(1, 11)))
