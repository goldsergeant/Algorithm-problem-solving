import collections
import sys

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for edge_num in range(1,M+1):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append((v,edge_num))
    graph[v].append((u,edge_num))

q=collections.deque([1])
visited=[False for _ in range(N+1)]
visited[1]=True
last_node=0

while q:
    node=q.popleft()
    last_node=node
    for adj,edge_num in graph[node]:
        if not visited[adj]:
            visited[adj]=True
            q.append(adj)

if N<=2:
    print(-1)
    exit()

if all(visited[1:]): #모든 정점들이 연결되어 있을때

    q=collections.deque()
    nodes=[]
    edge_nums=[]
    visited=[False for _ in range(N+1)]
    visited[last_node]=True
    for adj,edge_num in graph[last_node]:
        q.append(adj)
        visited[adj]=True
        break

    while q:
        node=q.popleft()
        nodes.append(node)

        for adj,edge_num in graph[node]:
            if not visited[adj]:
                visited[adj]=True
                q.append(adj)
                edge_nums.append(edge_num)

    print(1,N-1)
    print(last_node)
    print(*nodes)
    print(*edge_nums)

else: # 정점들이 연결되어 있지 않을 때
    connect_cnt=0
    visited=[False for _ in range(N+1)]
    nodes1,nodes2=[],[]
    edge_nums1,edge_nums2=[],[]

    for i in range(1,N+1):
        if not visited[i]:
            q=collections.deque([i])
            visited[i]=True
            connect_cnt+=1
            while q:
                node=q.popleft()
                if connect_cnt==1:
                    nodes1.append(node)
                elif connect_cnt==2:
                    nodes2.append(node)

                for adj,edge_num in graph[node]:
                    if not visited[adj]:
                        visited[adj]=True
                        q.append(adj)
                        if connect_cnt==1:
                            edge_nums1.append(edge_num)
                        elif connect_cnt==2:
                            edge_nums2.append(edge_num)

    if connect_cnt!=2 or len(nodes1)==len(nodes2):
        print(-1)
        exit()

    print(len(nodes1),len(nodes2))
    print(*nodes1)
    print(*edge_nums1)
    print(*nodes2)
    print(*edge_nums2)