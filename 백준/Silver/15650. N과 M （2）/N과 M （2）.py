import sys

n,m=map(int,sys.stdin.readline().split())
answer=[]

def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))

    for i in range(start,n+1):
        if i not in answer:
            answer.append(i)
            dfs(i)
            answer.pop()

dfs(1)



