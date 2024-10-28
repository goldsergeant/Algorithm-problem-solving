T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K=int(input())
    st=input()
    arr=[]
    for i in range(len(st)):
        arr.append(st[i:])

    # print(arr)
    if K<len(arr):
        print(f'#{test_case} {sorted(arr)[K-1]}')
    else:
        print(f'#{test_case} None')