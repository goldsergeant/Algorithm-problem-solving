import heapq
import sys

n = int(input())
wires = []
dest_wires=[]
dp=[1 for i in range(n)]
for i in range(n):
    wires.append(list(map(int, sys.stdin.readline().split())))

wires.sort(key=lambda x:x[0])
for wire in wires:
    dest_wires.append(wire[1])

for i in range(n):
    for j in range(i):
        if dest_wires[i]>dest_wires[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))