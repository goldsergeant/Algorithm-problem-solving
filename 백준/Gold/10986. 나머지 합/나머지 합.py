import sys
from math import comb

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
t_sum = [numbers[0]]
answer=0

for i in range(1, N):
    num = t_sum[i - 1] + numbers[i]
    t_sum.append(num)
mods_of_t_sum=[i%M for i in t_sum]

for num in set(mods_of_t_sum):
    answer+=comb(mods_of_t_sum.count(num),2)

answer+=mods_of_t_sum.count(0)
print(answer)