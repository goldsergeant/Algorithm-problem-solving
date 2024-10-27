import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    days = list(map(int, input().split()))
    visited=[False for _ in range(max(days)+P+1)]
    for day in days:
        visited[day] = True

    left=0
    right=0
    answer=1
    cnt=0

    while right<len(visited):
        if visited[right]:
            right+=1
            cnt+=1
        else:
            if P==0:
                if not visited[left]:
                    P+=1
                left+=1
                cnt-=1
                # P+=1
            else:
                right+=1
                P-=1
                cnt+=1
        answer=max(answer,cnt)
    print(f'#{test_case} {answer}')