def solution(info, edges):
    global answer,sheep,wolf
    tree = [[] for _ in range(len(info))]
    for u,v in edges:
        tree[u].append(v)

    answer=0
    sheep=1
    wolf=0
    def dfs(cur,adj_nodes):
        global answer,sheep,wolf
        answer=max(answer,sheep)
        for next_node in tree[cur]:
            adj_nodes.add(next_node)

        for next_node in adj_nodes:
            if info[next_node]==0:
                sheep+=1
                dfs(next_node,adj_nodes.difference(set([next_node])))
                sheep-=1
            elif sheep>wolf+1:
                wolf+=1
                dfs(next_node,adj_nodes.difference(set([next_node])))
                wolf-=1

    dfs(0,set())
    return answer
