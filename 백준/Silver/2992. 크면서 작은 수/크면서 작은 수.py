import sys

X=input()
answer=str(sys.maxsize)
visited=[False for _ in range(len(X)+1)]
def dfs(num,depth):
    global answer
    if depth==len(X):
       if X<num< answer:
           answer=num
       return

    for i in range(len(X)):
        if visited[i]:
            continue

        visited[i]=True
        dfs(num+X[i],depth+1)
        visited[i]=False

for i in range(len(X)):
    visited[i]=True
    dfs(X[i],1)
    visited[i]=False

print(answer if answer <str(sys.maxsize) else 0)
