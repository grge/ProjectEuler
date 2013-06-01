import inspect
import argparse
import sys
import re
from lib import Problem
import problems

parser = argparse.ArgumentParser(description='Run, test and benchmark Project Euler problems')
parser.add_argument('problems', metavar='N', type=int, nargs='*',
                           help='List of Project Euler problem numbers to run.')
args = parser.parse_args()
class_names = ["Problem_%d" % i for i in args.problems]

results = [0,0]
ttime = 0
def class_sort_key(named_class):
    return int(re.search(r'[0-9]+$', named_class[0]).group(0))

def class_filter(cls):
    return inspect.isclass(cls) and issubclass(cls, Problem) and cls != Problem

for name, obj in sorted(inspect.getmembers(problems, class_filter), key=class_sort_key):
    if not class_names or name in class_names:
        test = obj().test()
        bool_result = 1 if test[2] else 0
        results[bool_result] += 1
        status = ("Fail", "Pass")[bool_result]
        time = round(test[1]*1000,4)
        ttime += time
        print("%s: %s\nAnswer = %s\nTime = %s ms\n" % (name, status, test[0], time))
print("Total Time: %s ms" % ttime)

if results[0]:
    print("Failed tests: %s of %s" % (results[0], sum(results)))

