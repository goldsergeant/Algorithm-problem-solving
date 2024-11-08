# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
import collections

for test_case in range(1, 10 + 1):
    input_length, root=map(int, input().split())
    graph=collections.defaultdict(list)
    inp=list(map(int,input().split()))
    for i in range(0,input_length,2):
        u,v=inp[i],inp[i+1]
        graph[u].append(v)

    q=collections.deque([root])
    answer=0
    visited=[False for _ in range(100+1)]
    visited[root]=True
    while q:
        tmp=0
        for _ in range(len(q)):
            node=q.popleft()

            tmp=max(tmp,node)

            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node]=True
                    q.append(next_node)
        answer=tmp
        
    print(f'#{test_case} {answer}')