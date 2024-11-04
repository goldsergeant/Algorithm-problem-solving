T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    jump_boards=list(map(int,input().split()))
    jump_boards.sort()

    tmp1=[]
    tmp2=[]
    for i in range(len(jump_boards)):
        if i%2==0:
            tmp1.append(jump_boards[i])
        else:
            tmp2.append(jump_boards[i])

    optimized_boards=tmp1+tmp2[::-1]+tmp1+tmp2[::-1]

    answer=0
    for i in range(1,len(optimized_boards)):
        answer=max(answer,abs(optimized_boards[i]-optimized_boards[i-1]))

    print(f'#{test_case} {answer}')