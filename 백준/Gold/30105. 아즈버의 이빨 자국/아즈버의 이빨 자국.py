import collections
import itertools
import sys

N = int(sys.stdin.readline())
numbers = [*map(int, sys.stdin.readline().split())]
answer = []
dic=collections.defaultdict(set)

for i in range(N):
    for j in range(i+1,N):
        diff=numbers[j]-numbers[i]
        dic[diff].add(numbers[i])
        dic[diff].add(numbers[j])

for key,s in dic.items():
    if len(s)==N:
        answer.append(key)

print(len(answer))
print(*sorted(answer))