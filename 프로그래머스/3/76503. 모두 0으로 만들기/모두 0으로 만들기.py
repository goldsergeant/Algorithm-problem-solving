import collections
import sys

sys.setrecursionlimit(1000000)


def solution(a, edges):
    global answer
    def dfs(node):
        global answer
        visited[node] = True
        num=a[node]
        for next_node in tree[node]:
            if not visited[next_node]:
                tmp=dfs(next_node)
                answer+=abs(tmp)
                num+=tmp

        return num
    tree = collections.defaultdict(list)
    visited = [False for _ in range(len(a))]
    answer=0
    for u,v in edges:
        tree[u].append(v)
        tree[v].append(u)

    if dfs(0)!=0:
        return -1

    return answer

print(solution([-5,0,2,1,2],	[[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0],	[[0,1],[1,2]]))
