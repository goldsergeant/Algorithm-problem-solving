def solution(n, arr1, arr2):
    answer = []
    board1=[[] for _ in range(n)]
    board2=[[] for _ in range(n)]
    for i in range(n):
        board1[i]=list(map(int,bin(arr1[i])[2:].zfill(n)))
        board2[i]=list(map(int,bin(arr2[i])[2:].zfill(n)))

    for i in range(n):
        arr=[]
        for j in range(n):
            if board1[i][j] or board2[i][j]:
                arr.append('#')
            else:
                arr.append(' ')
        answer.append(''.join(arr))

    return answer

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))