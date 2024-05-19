import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    books_want=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
    books_want.sort(key=lambda x:(x[1],x[0],))
    visited=[False for _ in range(N+1)]
    answer=0
    for a,b in books_want:
        for i in range(a,b+1):
            if not visited[i]:
                visited[i]=True
                answer+=1
                break

    print(answer)