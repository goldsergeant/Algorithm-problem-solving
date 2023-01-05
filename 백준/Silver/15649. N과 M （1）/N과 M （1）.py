import sys

n,m=map(int,sys.stdin.readline().split())

def dfs(depth,s):
    if depth>=m:
        print(s.lstrip())
        return

    for i in range(1,n+1):
        if str(i) not in s:
            dfs(depth+1,s+" "+str(i))

dfs(0,'')





