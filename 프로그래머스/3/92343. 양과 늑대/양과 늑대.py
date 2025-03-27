def solution(info, edges):
    global answer
    tree = [[] for _ in range(len(info))]
    for u, v in edges:
        tree[u].append(v)
    visited = [False for _ in range(1 << 17)]
    answer=0

    def dfs(bit_state, wolf, sheep):
        global answer
        visited[bit_state] = True
        answer = max(answer, sheep)

        for i in range(len(info)):
            if not bit_state & (1 << i):  # 방문하지 않았다면
                continue

            for next_node in tree[i]:
                if visited[bit_state | (1 << next_node)]:
                    continue

                if info[next_node] == 0:
                    dfs(bit_state|(1<<next_node), wolf, sheep + 1)
                elif sheep > wolf + 1:
                    dfs(bit_state|(1<<next_node), wolf + 1, sheep)

    dfs(1,0,1)
    return answer