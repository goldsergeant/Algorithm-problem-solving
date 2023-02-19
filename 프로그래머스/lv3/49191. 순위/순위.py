import collections
def solution(n, results):
    graph_win=collections.defaultdict(list)
    graph_lose=collections.defaultdict(list)
    answer=0
    for winner,loser in results:
        graph_win[winner].append(loser)
        graph_lose[loser].append(winner)

    def dfs(start,visited,graph):
        stack=collections.deque()
        stack.append(start)
        depth=0
        while stack:
            next=stack.pop()
            if next not in visited:
                visited.append(next)
                depth+=1
                for vertex in graph[next]:
                    stack.append(vertex)
        return depth-1


    for i in range(1,n+1):
        visited1=[]
        visited2=[]
        if dfs(i,visited1,graph_win)+dfs(i,visited2,graph_lose)==n-1:
            answer+=1
    return answer