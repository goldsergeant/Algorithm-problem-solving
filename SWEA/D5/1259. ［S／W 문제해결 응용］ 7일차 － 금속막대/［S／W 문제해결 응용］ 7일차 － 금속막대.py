
def dfs():
    global answer
    flag=False

    for i in range(N):
        if not visited[i]:
            if connected_screws[-1]==screws[i][0]:
                connected_screws.extend(screws[i])
                flag=True
                visited[i]=True
                dfs()
                connected_screws.pop()
                connected_screws.pop()
                visited[i]=False

    if not flag and len(connected_screws)>len(answer):
        answer=connected_screws.copy()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    arr=list(map(int,input().split()))
    screws=[]
    for i in range(1,len(arr),2):
        screws.append([arr[i-1],arr[i]])

    visited=[False for _ in range(N)]
    connected_screws=[]
    answer=[]

    for i in range(N):
        visited[i]=True
        connected_screws.extend(screws[i])
        dfs()
        visited[i]=False
        connected_screws.pop()
        connected_screws.pop()
    
    tmp=' '.join(map(str,answer))
    print(f'#{test_case} {tmp}')