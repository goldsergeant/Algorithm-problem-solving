import sys
sys.setrecursionlimit(100000)

T=int(sys.stdin.readline())

def dfs(num):
    global cnt
    visited[num]=True
    next_num=numbers[num]
    if not visited[next_num]:
        dfs(next_num)

    elif not done[next_num]:
        i=next_num
        while i!=num:
            i=numbers[i]
            cnt+=1
        cnt+=1


    done[num]=True

for _ in range(T):
    N=int(sys.stdin.readline())
    numbers=[0]+list(map(int,sys.stdin.readline().split()))
    visited=[False]*(N+1)
    done=[False]*(N+1)
    cnt=0
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)

    print(N-cnt)
