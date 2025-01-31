import collections


def solution(m, n, board):
    global answer
    answer = 0

    for i in range(len(board)):
        board[i] = list(board[i])

    def delete_blocks():

        deleted_cnt=0
        will_delete = [[False for _ in range(n)] for _ in range(m)]
        for i in range(len(board) - 1):
            for j in range(len(board[i]) - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] and board[i][j]!='':
                    will_delete[i][j] = True
                    will_delete[i][j + 1] = True
                    will_delete[i + 1][j] = True
                    will_delete[i + 1][j + 1] = True

        for i in range(m):
            for j in range(n):
                if will_delete[i][j]:
                    board[i][j] = ''
                    deleted_cnt+=1

        return deleted_cnt

    def drop_blocks():
        for i in range(m-2, -1, -1):
            for j in range(n):
                if board[i][j]=='':
                    continue

                for target_row in range(m-1,i,-1):
                    if board[target_row][j]=='':
                        board[i][j],board[target_row][j]='',board[i][j]
                        break

    while True:
        deleted_cnt=delete_blocks()
        if deleted_cnt==0:
            break

        answer+=deleted_cnt
        drop_blocks()
    return answer