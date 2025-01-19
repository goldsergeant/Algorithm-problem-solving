import sys

N = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
growths = list(map(int, sys.stdin.readline().split()))
tree=[[heights[i],growths[i]] for i in range(N)]
tree.sort(key=lambda x:x[1])
answer=0
for i in range(N):
    h,g=tree[i]
    answer+=h+g*i

print(answer)