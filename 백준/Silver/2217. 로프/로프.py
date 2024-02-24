import sys

N=int(sys.stdin.readline())
ropes=list(int(sys.stdin.readline()) for _ in range(N))
ropes.sort()
answer=0
for i in range(N):
    answer=max(answer,ropes[i]*(N-i))

print(answer)