
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L = int(input())
    N = int(input())
    t_sum=[0 for _ in range(N+1)]
    peeks=[]
    for i in range(N):
        s, e = map(int, input().split())
        peeks.append((s,e))
        t_sum[i+1]=t_sum[i]+e-s

    answer=0
    for i in range(N):
        left=i
        right=N-1

        while left<=right:
            mid=(left+right)//2
            if peeks[mid][1]-peeks[i][0]<=L:
                left=mid+1
            else:
                right=mid-1

        tmp=t_sum[left]-t_sum[i]
        if left<N:
            tmp+=max(0,peeks[i][0]+L-peeks[left][0])
        answer=max(answer,tmp)

    # print(t_sum)
    print(f'#{test_case} {answer}')