import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
ropes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ropes.sort()
check_rope = [False for _ in range(N)]
arr = [ropes[0][1]]
real_rope_idx = [0 for _ in range(N)]
real_rope=[]
for i in range(1, N):
    a, b = ropes[i]
    if b > arr[-1]:
        arr.append(b)
        real_rope_idx[i] = len(arr) - 1
    else:
        idx = bisect_left(arr, b)
        arr[idx] = b
        real_rope_idx[i] = idx

target=len(arr)-1
for i in range(N-1,-1,-1):
    if real_rope_idx[i]==target:
        target-=1
        real_rope.append(ropes[i])

for a,b in real_rope:
    idx=bisect_left(ropes,a,key=lambda x:x[0])
    check_rope[idx]=True

print(N - len(arr))
answer = []
for i in range(len(ropes)):
    if not check_rope[i]:
        answer.append(ropes[i][0])
print(*answer, sep='\n')
# print(arr)
