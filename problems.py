from lib import *
from math import sqrt
import re


class Problem_1(Problem):
    known_answer = 233168
    def solve(self):
        return sum([i for i in range(1, 1000) if not (i % 3 and i % 5)])

class Problem_2(Problem):
    known_answer = 4613732
    def solve(self):
        return sum([i for i in fibs_up_to(4e6) if not i % 2])

class Problem_3(Problem):
    known_answer = 6857
    def solve(self):
        s = sieve()
        n = 600851475143
        for i in reversed(range(1, int(sqrt(n)))):
            if (not n % i) and s.is_prime(i):
                return i

class Problem_4(Problem):
    known_answer = 906609
    def solve(self):
        def palindrome_products(a, b):
            for i in range(a, b):
                for j in range(a, b):
                    p = str(i * j)
                    if p == p[::-1]:
                        yield i * j
        return max([i for i in palindrome_products(100,999)])

class Problem_5(Problem):
    known_answer = 232792560
    def solve(self):
        s = sieve()
        new_factors = {k:0 for k in range(1, 20)}
        for n in range(1, 20):
            for p, i in s.group_factors(n):
                if new_factors[p] < i:
                    new_factors[p] = i
        return product([k**v for k, v in new_factors.items()])
    
class Problem_6(Problem):
    known_answer = 25164150
    def solve(self):
        nums = range(1, 101)
        return (sum(nums)**2 - sum(n**2 for n in nums))

class Problem_7(Problem):
    known_answer = 104743
    def solve(self):
        return sieve().nth_prime(10001)

@data('problem8')
class Problem_8(Problem):
    known_answer = 40824
    def solve(self):
        n = re.sub(r'\s+', '', self.data)
        return max([product(map(int,n[i:i+5])) for i in range(len(n)-4)])

class Problem_9(Problem):
    known_answer = 31875000
    def solve(self):
        for i in range(2, 1000):
            for j in range(i, 1000):
                for k in range(j, 1000):
                    if i**2 + j**2 == k**2 and i + j + k == 1000:
                        return i * j * k

class Problem_10(Problem):
    known_answer = 142913828922 
    def solve(self):
        return sum(sieve().prime_generator(lambda i, p: i < int(2e6)))

@data('problem11')
class Problem_11(Problem):
    known_answer = 70600674
    def solve(self):
        def iter_grid_products(grid, prod_length):
            for y in range(len(grid)):
                vert_cond = y < len(grid) - prod_length + 1
                for x in range(len(grid[y])):
                    horz_cond = x < len(grid[y]) - prod_length + 1
                    diag_lr_cond = horz_cond and vert_cond
                    diag_rl_cond = horz_cond and ( y >= prod_length - 1)
                    if horz_cond: 
                        yield product([ grid[y][x + i] for i in range(prod_length)]) 
                    if vert_cond: 
                        yield product([ grid[y + i][x] for i in range(prod_length)]) 
                    if diag_lr_cond: 
                        yield product([ grid[y + i][x + i] for i in range(prod_length)]) 
                    if diag_rl_cond: 
                        yield product([ grid[y - i][x + i] for i in range(prod_length)]) 
        # split into cells
        lines = (re.split(r'\s', line) for line in re.split(r'\n', self.data.strip()))
        # parse integers
        grid = list(map(lambda line : list(map(lambda element : int(element), line)), lines))
        return max([i for i in iter_grid_products(grid, 4)])
        
class Problem_12(Problem):
    known_answer = 76576500 
    def solve(self):
        triangle = 1
        i = 2
        while sieve().num_divisors(triangle) < 500:
            triangle += i
            i += 1
        return triangle

@data('problem13')
class Problem_13(Problem):
    known_answer = 5537376230
    def solve(self):
        rows = re.split(r'\s', self.data.strip())
        return int(str(sum([int(i) for i in rows]))[:10])

class Problem_14(Problem):
    known_answer = 837799
    def solve(self):
        def simple_collatz(limit):
            (s, l) = (0, 0)
            cache = [0] * int(limit)
            cache[1] = 1
            for i in range(2, int(limit)):
                seq_l = 1
                seq = i
                while (seq != 1 and seq >= i):
                    if seq % 2:
                        seq = seq*3 + 1
                    else:
                        seq /= 2
                    seq_l += 1
                cache[i] = seq_l + cache[seq]
                if cache[i] > l:
                    (s, l) = (i, cache[i])
            return s
        return simple_collatz(1e06)

class Problem_15(Problem):
    known_answer = 1378465
    def solve(self):
        return choose(40, 20)

class Problem_16(Problem):
    known_answer = 1366
    def solve(self):
        return sum(int(c) for c in str(2**1000))

class Problem_17(Problem):
    known_answer = 21124
    def solve(self):
        units = ['','one','two','three','four','five','six','seven','eight',
                 'nine','ten', 'eleven','twleve','thirteen','fourteen',
                 'fifteen','sixteen','seventeen','eighteen','nineteen'] 
        tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

        def num_to_string(num):
            if num == 1000: 
                return 'one thousand'
            if num >= 100:
                (a, b) = (int(num / 100), num % 100)
                if b:
                    return '%s hundred and %s' % (units[a], num_to_string(b))
                else:
                    return '%s hundred' % units[a]
            if num >= 20:
                (a, b) = (int(num / 10), num % 10)
                return '%s %s' % (tens[a], units[b]) if b else tens[a]
            return units[num]
        return len(re.sub(r' ','',''.join(num_to_string(n) for n in range(1, 1001))))

@data('problem18')
class Problem_18(Problem):
    known_answer = 1074
    def solve(self):
        data = [list(map(int, re.split(' ', line))) for line in re.split('\n',self.data.strip())]
        for i in range(1,len(data)):
            for j in range(len(data[i])):
                if j == 0:
                    data[i][0] += data[i-1][0]
                elif j == i:
                    data[i][j] += data[i-1][i-1]
                else:
                    data[i][j] += max(data[i-1][j], data[i-1][j-1])
        return max(data[-1])
            
class Problem_19(Problem):
    known_answer = 171
    def solve(self):
        def sunday_the_first_generator():
            start_day = 0
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for year in range(1900,2001):
                leap = (not (year % 4)) and (year % 100) and (not (year % 400))
                for month in range(0,12):
                    if start_day % 7 == 6 and year > 1900: 
                        yield year, month
                    start_day += days_in_month[month] + {True:1, False:0}[leap and month==1]
        return len(list(sunday_the_first_generator()))

class Problem_20(Problem):
    known_answer = 648
    def solve(self):
        return sum(int(c) for c in str(product(range(1, 101))))

class Problem_21(Problem):
    def solve(self):
        pass 

class Problem_22(Problem):
    def solve(self):
        pass

class Problem_23(Problem):
    def solve(self):
        pass

class Problem_24(Problem):
    def solve(self):
        pass

class Problem_28(Problem):
    known_answer = 669171001 
    def solve(self):
        return sum([(i+1)**2 * 4 - 6*i for i in range(2, 1001, 2)]) + 1

class Problem_28(Problem):
    known_answer = 49 
    def solve(self):
        count = 0
        for i in range(1, 10):
            j = 1
            while len(str(i**j)) == j:
                count += 1
                j += 1
        return count

@data('problem67')
class Problem_67(Problem_18):
    known_answer = 7273

class Problem_92(Problem):
    known_answer = 8581146
    def solve(self):
        def f(n):
            yield n
            while n != 89 and n != 1:
                n = sum(map(lambda x : int(x)**2, str(n)))
                yield n
        count = 0
        for i in range(1, int(1e7)):
            for n in f(i):
                pass
            if n == 89:
                count += 1

        return count
