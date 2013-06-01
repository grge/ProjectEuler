from lib import *

class Problem01(Problem):
    def solve(self):
        return sum([i for i in range(1, 1000) if not (i % 3 and i % 5)])

class Problem02(Problem):
    def solve(self):
        return sum([i for i in fibs_up_to(4e6) if not i % 2])

