import collections
import sys

def dfs(room,money,visited):
    global answer
    if room==N:
        answer= True
        return

    for next_room in graph[room]:
        if not visited[next_room]:
            alphabet,price=room_info[next_room]
            if alphabet=='E':
                visited[next_room]=True
                dfs(next_room,money,visited)
                visited[next_room]=False
            elif alphabet=='L':
                visited[next_room]=True
                dfs(next_room,max(money,price),visited)
                visited[next_room]=False
            else:
                if money>=price:
                    visited[next_room]=True
                    dfs(next_room,money-price,visited)
                    visited[next_room]=False


while True:
    N=int(sys.stdin.readline())
    answer=False
    if N==0:
        break

    graph=collections.defaultdict(list)
    room_info=dict()
    for i in range(1,N+1):
        arr=list(sys.stdin.readline().split())
        alphabet,price,next_rooms=arr[0],int(arr[1]),list(map(int,arr[2:-1])),
        room_info[i]=(alphabet,price)
        graph[i].extend(next_rooms)

    visited=[False for _ in range(N+1)]
    visited[1]=True
    dfs(1,0,visited)
    print('Yes' if answer else 'No')


