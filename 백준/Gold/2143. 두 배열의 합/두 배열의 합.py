import bisect
import itertools
import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
answer=0
a_total=[]
b_total=[]
for left,right in itertools.combinations(range(len(a)+1),2):
    a_total.append(sum(a[left:right]))
for left,right in itertools.combinations(range(len(b)+1),2):
    b_total.append(sum(b[left:right]))
b_total.sort()

for a_sum in a_total:
    need_sum=T-a_sum
    left=bisect.bisect_left(b_total,need_sum)
    right=bisect.bisect_right(b_total,need_sum)
    answer+=right-left

print(answer)

