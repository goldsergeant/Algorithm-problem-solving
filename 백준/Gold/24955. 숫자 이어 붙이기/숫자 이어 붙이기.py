import collections
import sys

sys.setrecursionlimit(1000 + 1)

MOD_NUM = 1000000007
N, Q = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)


def connect_num(a, b):
    temp = b
    b_digit = 0
    while temp > 0:
        b_digit += 1
        temp //= 10
    while b_digit > 0:
        a *= 10
        b_digit -= 1
    return a + b


def bfs(start,end):
    q=collections.deque([(start,nums[start])])
    visited=[False]*(N+1)
    visited[start]=True
    while q:
        node,num=q.popleft()
        if node==end:
            return num

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append((next_node,connect_num(num,nums[next_node])%MOD_NUM))

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a,b))
