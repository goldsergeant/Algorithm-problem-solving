import sys

A,B,C=map(int,sys.stdin.readline().split())
visited=[[[False for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]
answer=[]
send=[0,0,1,1,2,2]
receive=[1,2,0,2,0,1]
limit=[A,B,C]
def dfs(a,b,c):
    if a==0:
        answer.append(c)

    visited[a][b][c]=True
    for i in range(6):
        next_arr = [a, b, c]

        next_arr[receive[i]]+=next_arr[send[i]]
        next_arr[send[i]]=0

        if next_arr[receive[i]]>limit[receive[i]]:
            next_arr[send[i]]+=next_arr[receive[i]]-limit[receive[i]]
            next_arr[receive[i]]=limit[receive[i]]

        n_a,n_b,n_c=next_arr
        if not visited[n_a][n_b][n_c]:
            visited[n_a][n_b][n_c]=True
            dfs(n_a,n_b,n_c)



dfs(0,0,C)
print(*sorted(answer))