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
import collections

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

'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# import sys
# sys.stdin = open("input.txt", "r")

def can_play(p,day,next_time):
    if day==M:
        return closest_hotel_and_airport_distance[start_node]+next_time<=540
    return closest_hotel_and_airport_distance[p]+next_time<=540


def dfs(node,stf,day,time):
    global answer_stf,answer_nodes
    if nodes_info[node][0]=='A' and day==M and time!=0:
        if stf>answer_stf:
            answer_stf=stf
            answer_nodes=visited_nodes.copy()
        return

    flag=False
    for next_node in range(1,N+1):
        if node==next_node:
            continue
        if nodes_info[next_node][0]!='P':
            continue

        if not visited[next_node]:
            next_time=time+distance[node][next_node]+nodes_info[next_node][1]
            next_stf=stf+nodes_info[next_node][2]

            if next_time>540:
                continue
            visited[next_node]=True
            visited_nodes.append(next_node)
            dfs(next_node,next_stf,day,next_time)
            visited[next_node]=False
            visited_nodes.pop()
            flag=True

    if not flag:
        if day==M:
            next_time=time+distance[node][start_node]
            if next_time>540:
                return
            visited_nodes.append(start_node)
            dfs(start_node,stf,day,next_time)
            visited_nodes.pop()
        else:
            for next_node in range(1,N+1):
                if nodes_info[next_node][0]!='H':
                    continue
                next_time=time+distance[node][next_node]
                if next_time>540:
                    continue
                visited_nodes.append(next_node)
                dfs(next_node,stf,day+1,0)
                visited_nodes.pop()



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    distance = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    answer_stf=0
    answer_nodes=[]
    for i in range(1, N):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            distance[i][i + j + 1] = arr[j]
            distance[i + j + 1][i] = arr[j]

    nodes_info=dict()
    start_node=0
    for i in range(1,N+1):
        arr= list(input().split())
        arr = list(map(lambda x: int(x) if x.isdigit() else x,arr))
        nodes_info[i]=arr
        if arr[0]=='A':
            start_node=i

    # for i in range(1,N+1):
    #     if nodes_info[i][0]=='P':
    #         for j in range(1,N+1):
    #             if nodes_info[j][0]=='H' or nodes_info[j][0]=='A':
    #                 closest_hotel_and_airport_distance[i]=min(closest_hotel_and_airport_distance[i],distance[i][j])

    visited = [0 for _ in range(N + 1)]
    visited_nodes=[]
    dfs(start_node,0,1,0)

    tmp= ' '.join(map(str,answer_nodes))
    print(f'#{test_case} {answer_stf} {tmp}')