import sys

N,M,B=map(int,sys.stdin.readline().split())
land=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=(sys.maxsize,-1)

for target in range(256+1):
    need_block=0
    remove_block=0
    for i in range(N):
        for j in range(M):
            if land[i][j]>target:
                remove_block+=land[i][j]-target
            else:
                need_block+= target - land[i][j]

    if need_block<=B+remove_block:
        time=remove_block*2+need_block
        if time<=answer[0]:
            answer=(time,target)

print(*answer)