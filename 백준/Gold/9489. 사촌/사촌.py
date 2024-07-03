import sys
import collections

while True:
    N,K=map(int,sys.stdin.readline().split())
    if N==0 and K==0:
        break

    tree=collections.defaultdict(list)
    numbers=[*map(int,sys.stdin.readline().split())]
    q=collections.deque([numbers[0]])
    parent=collections.defaultdict(int)
    nodes=[]
    for i in range(1,N):
        if not nodes:
            nodes.append(numbers[i])
            continue

        if nodes[-1]+1==numbers[i]:
            nodes.append(numbers[i])
        else:
            p=q.popleft()
            tree[p].extend(nodes)
            for node in nodes:
                q.append(node)
                parent[node]=p
            nodes=[numbers[i]]

    p = q.popleft()
    for node in nodes:
        tree[p].append(node)
        parent[node]=p


    answer=0
    k_p=parent[K]
    k_p_p=parent[k_p]
    for node in tree[k_p_p]:
        if node!=k_p:
            answer+=len(tree[node])

    print(answer)