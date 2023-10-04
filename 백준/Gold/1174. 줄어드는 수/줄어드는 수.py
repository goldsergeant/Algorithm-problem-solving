import itertools
import sys

n = int(sys.stdin.readline())
numbers = list(map(str,[i for i in reversed(range(10))]))
combies = []
for i in range(1, 11):
    for nums in itertools.combinations(numbers, i):
        combies.append(''.join(nums))

combies.sort(key=int)

try:
    print(combies[n-1])
except:
    print(-1)
