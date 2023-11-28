import collections
import heapq
import sys

T=int(sys.stdin.readline())

for _ in range(T):
    n,m,t=map(int,sys.stdin.readline().split())
    s,g,h=map(int,sys.stdin.readline().split())
    graph=collections.defaultdict(list)
    targets=[]
    check=[False]*(n+1)
    distance=[sys.maxsize]*(n+1)
    distance[s]=0

    for _ in range(m):
        a,b,d=map(int,sys.stdin.readline().split())
        graph[a].append((d,b))
        graph[b].append((d,a))

    for _ in range(t):
        targets.append(int(sys.stdin.readline()))

    q=[(0,s)]

    while q:
        cur_distance,cur_node=heapq.heappop(q)
        if cur_distance > distance[cur_node]:
            continue
        for next_distance,next_node in graph[cur_node]:
            new_distance=cur_distance+next_distance
            check_temp=check[cur_node]
            if (cur_node==g and next_node==h) or (cur_node==h and next_node==g):
                check_temp=True

            if new_distance<distance[next_node]:
                distance[next_node]=cur_distance+next_distance
                check[next_node]=check_temp
                heapq.heappush(q,(distance[next_node],next_node))
            if new_distance==distance[next_node] and not check[next_node] and check_temp:
                check[next_node]=check_temp
                heapq.heappush(q,(distance[next_node],next_node))


    answer=[]
    for node in targets:
        if check[node]:
            answer.append(node)

    print(*sorted(answer))
