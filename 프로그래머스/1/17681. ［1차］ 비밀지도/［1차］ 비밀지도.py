def solution(n, arr1, arr2):
    answer = []
    board=[0 for _ in range(n)]
    for i in range(n):
        board[i]=arr1[i]|arr2[i]
        
    for i in range(n):
        tmp=[]
        for j in range(n):
            if 1<<j&board[i]:
                tmp.append('#')
            else:
                tmp.append(' ')
        board[i]=''.join(tmp[::-1])
    return board

