import collections
import sys

def check(a_visit_bit):
    visited = [False for _ in range(N + 1)]
    q = collections.deque()
    a_inserted = False
    b_inserted=False
    a=0
    b=0
    for i in range(1, N + 1):
        if a_visit_bit&(1<<i): # a_visit_bit에 i가 있어야 함
            if not visited[i]:
                if not a_inserted:
                    a_inserted=True
                    q.append(i)
                    visited[i]=True
                    while q:
                        node=q.popleft()
                        a+=people[node]
                        for adj in graph[node]:
                            if not visited[adj] and a_visit_bit&(1<<adj):
                                visited[adj]=True
                                q.append(adj)

                else:
                    return sys.maxsize

    q.clear()
    for i in range(1,N+1):
        if not a_visit_bit&(1<<i):
            if not visited[i]:
                if not b_inserted:
                    b_inserted=True
                    q.append(i)
                    visited[i] = True
                    while q:
                        node = q.popleft()
                        b += people[node]
                        for adj in graph[node]:
                            if not visited[adj] and not a_visit_bit&(1<<adj):
                                visited[adj] = True
                                q.append(adj)

                else:
                    return sys.maxsize

    if not a_inserted or not b_inserted:
        return sys.maxsize
    return abs(a-b)

N=int(sys.stdin.readline())
people=[0]+list(map(int,sys.stdin.readline().split()))
answer=sys.maxsize
graph=collections.defaultdict(list)
for i in range(1,N+1):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(arr)):
        graph[i].append(arr[j])

for a_visit_bit in range(1,1<<N):
    answer=min(answer,check(a_visit_bit))

print(answer if answer<sys.maxsize else -1)