import sys
sys.setrecursionlimit(100000)

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
start=int(sys.stdin.readline())
answer=0
visited=[False]*n
def dfs(node,depth):
    global answer
    answer+=1

    for next_node in [node+arr[node],node-arr[node]]:
        if next_node<0 or next_node>n-1:
            continue
        if not visited[next_node]:
            visited[next_node]=True
            dfs(next_node,depth+1)

visited[start-1]=True
dfs(start-1,1)
print(answer)
