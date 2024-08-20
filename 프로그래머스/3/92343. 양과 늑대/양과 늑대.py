

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for u,v in edges:
        tree[u].append(v)

    def dfs(cur,visited_nodes:set,sheep,wolf):
        if info[cur]:
            wolf+=1
        else:
            sheep+=1

        if sheep<=wolf:
            return 0

        tmp_max_sheep=sheep

        for visited_node in visited_nodes:
            for next_node in tree[visited_node]:
                if next_node not in visited_nodes:
                    visited_nodes.add(next_node)
                    tmp_max_sheep=max(tmp_max_sheep,dfs(next_node,visited_nodes,sheep,wolf))
                    visited_nodes.remove(next_node)

        return tmp_max_sheep

    dfs(0,{0},1,0)

    return dfs(0,{0},0,0)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))