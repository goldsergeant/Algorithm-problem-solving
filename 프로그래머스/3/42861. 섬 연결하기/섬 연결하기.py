def solution(n, costs):
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    answer = 0
    costs.sort(key=lambda x: x[2])

    for a,b,c in costs:
        if find(a)!=find(b):
            union(a, b)
            answer+=c
    return answer
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))