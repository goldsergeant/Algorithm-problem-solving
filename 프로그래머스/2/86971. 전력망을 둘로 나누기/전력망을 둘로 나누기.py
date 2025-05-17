import sys
import collections
def solution(n, wires):
    global answer
    answer=sys.maxsize
    visited=[False for _ in range(n+1)]
    graph=collections.defaultdict(list)
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node):
        global answer
        visited[node]=True
        child_sum=0
        for adj in graph[node]:
            if not visited[adj]:
                adj_child_sum=dfs(adj)
                child_sum+=adj_child_sum
                answer=min(answer,abs((n-adj_child_sum)-adj_child_sum))
                
        
        return child_sum+1
    dfs(1)
        
    return answer
    