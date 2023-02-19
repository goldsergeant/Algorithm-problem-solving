import collections
def solution(tickets):
    # 1. 그래프 생성
    graph = collections.defaultdict(list)

    for (start, end) in tickets:
        graph[start].append(end)

        # 2. 시작점 - [끝점] 역순으로 정렬
    for node in graph.keys():
        graph[node].sort(reverse=True)

    # 3. DFS 알고리즘으로 path를 만들어줌.
    stack=collections.deque()
    stack.append("ICN")
    answer=[]

    while stack:
        next=stack[-1]

        if graph[next]==[]:
            answer.append(stack.pop())
        else:
            stack.append(graph[next].pop())
    return answer[::-1]
