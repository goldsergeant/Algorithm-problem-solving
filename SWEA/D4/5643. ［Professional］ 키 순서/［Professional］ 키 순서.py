# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

# import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open("input.txt", "r")

import collections


def topology_sort(q,graph,in_degree,related_nodes):
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            related_nodes[next_node].update(related_nodes[node])
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())
    in_degree = [0 for _ in range(N + 1)]
    reverse_in_degree = [0 for _ in range(N + 1)]
    forward_graph = collections.defaultdict(list)
    reverse_graph = collections.defaultdict(list)
    forward_relate_nodes = [{i} for i in range(N + 1)]
    reverse_relate_nodes = [{i} for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        forward_graph[a].append(b)
        in_degree[b] += 1
        reverse_graph[b].append(a)
        reverse_in_degree[a] += 1
    answer = 0

    q1 = collections.deque()
    q2 = collections.deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q1.append(i)
        if reverse_in_degree[i] == 0:
            q2.append(i)

    topology_sort(q1,forward_graph,in_degree,forward_relate_nodes)
    topology_sort(q2,reverse_graph,reverse_in_degree,reverse_relate_nodes)

    for i in range(1, N + 1):
        if len(forward_relate_nodes[i])+len(reverse_relate_nodes[i])-1==N:
            answer+=1

    print(f'#{test_case} {answer}')
