import collections

A, B = 0, 99

def dfs(node):
    if node==B:
        return True
    if dp[node]!=-1:
        return dp[node]

    dp[node]=False

    for next_node in graph[node]:
            dp[node]=dp[node] or dfs(next_node)
    return dp[node]

for _ in range(1,10+1):
    test_case, road_cnt= map(int, input().split())
    graph=collections.defaultdict(list)
    road_info=list(map(int,input().split()))
    dp=[-1 for _ in range(100)]
    for i in range(0,len(road_info),2):
        graph[road_info[i]].append(road_info[i+1])

    print(f'#{test_case} {int(dfs(A))}')