import collections
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
tree = collections.defaultdict(list)
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    node = arr[0]
    for i in range(1, len(arr)-1, 2):
        tree[node].append((arr[i],arr[i+1]))

visited=[False for _ in range(N+1)]
long_tup=(0,0)

def get_long_node(node,distance):
    global long_tup
    if distance>long_tup[1]:
        long_tup=(node,distance)
    visited[node] = True
    for next_node,next_distance in tree[node]:
        if not visited[next_node]:
            get_long_node(next_node,distance+next_distance)
def get_distance(node):
    visited[node]=True
    max_distance=0
    for next_node,next_distance in tree[node]:
        if not visited[next_node]:
            max_distance=max(max_distance, get_distance(next_node) + next_distance)

    return max_distance

get_long_node(1,0)
# print(long_tup)
visited=[False for _ in range(N+1)]
print(get_distance(long_tup[0]))
