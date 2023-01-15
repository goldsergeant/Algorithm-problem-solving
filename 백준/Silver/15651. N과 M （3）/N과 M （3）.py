import sys

n,m=map(int,sys.stdin.readline().split())
answer=[]

def dfs():
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return

    for i in range(1,n+1):
        answer.append(i)
        dfs()
        answer.pop()

dfs()



