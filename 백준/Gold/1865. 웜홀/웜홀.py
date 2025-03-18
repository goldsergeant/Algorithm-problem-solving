import collections
import sys
from heapq import heappush, heappop

def bellman_ford():
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(N):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(len(edges)):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == N - 1:
                    return True
    return False

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    edges=[]
    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, sys.stdin.readline().split())
        edges.append((s, e, -t))
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[1]=0
    if bellman_ford():
        print("YES")
    else:
        print("NO")