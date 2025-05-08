import sys

N = int(sys.stdin.readline())
weights=list(map(int,sys.stdin.readline().split()))
weights.sort()
last_n=1
for w in weights:
    if w>last_n:
        print(last_n)
        exit()
    last_n+=w
print(last_n)