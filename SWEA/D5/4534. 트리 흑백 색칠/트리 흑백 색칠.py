import collections

BLACK = 0
WHITE = 1
MOD_NUM = 1000000007


def dfs(node):
    visited[node] = True

    for next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            adj_info = dfs(next_node)
            b, w = adj_info[BLACK], adj_info[WHITE]
            dp[node][BLACK] = dp[node][BLACK] * w
            dp[node][WHITE] = dp[node][WHITE] * (b + w)

    return dp[node]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    tree = collections.defaultdict(list)
    for _ in range(N - 1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)

    dp = [[1, 1] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    print(f'#{test_case} {sum(dfs(1))%MOD_NUM}')
    # print(dp)
