from lib import load_data
import re

rows = re.split(r'\s', load_data("problem13").strip())

# done the long way, in the spirit of the challenge.
data = [list(line) for line in rows]
big_sum = []
carry = 0
for i in range(50,0,-1):
    total = sum([int(row[i-1]) for row in data]) + carry
    big_sum.insert(0, str(total % 10))
    carry = int(total / 10)
big_sum.insert(0,str(carry))
print ''.join(big_sum)[:10]

# done the pythonic way
print str(sum([int(i) for i in rows]))[:10]
