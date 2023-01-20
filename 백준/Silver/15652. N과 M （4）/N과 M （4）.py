import sys

n,m=map(int,sys.stdin.readline().split())
def dfs(st,depth):
    if depth>m:
        print(st.strip())
        return
    for i in range(1,n+1):
        if len(st)==0 or i>=int(st[-1]):
            dfs(st+' '+str(i),depth+1)
dfs('',1)

