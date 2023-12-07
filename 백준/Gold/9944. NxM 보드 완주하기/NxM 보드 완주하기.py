import sys

test_case = 1
direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def dfs(row, col, dir, level, total_empty, depth):
    global answer
    if total_empty == depth:
        answer = min(answer, level)
        return

    if dir==-1:
        for i in range(4):
            n_r, n_c = row + direct[i][0], col + direct[i][1]
            if n_r < 0 or n_c < 0 or n_r > n - 1 or n_c > m - 1:
                continue
            if board[n_r][n_c] == '*':
                continue

            board[n_r][n_c] = '*'
            dfs(n_r, n_c, i, level+1, total_empty, depth + 1)
            board[n_r][n_c] = '.'

    else:
        n_r,n_c= row+direct[dir][0], col+direct[dir][1]
        if 0<=n_r<=n-1 and 0<=n_c<=m-1 and board[n_r][n_c]=='.':
            board[n_r][n_c]='*'
            dfs(n_r, n_c, dir, level, total_empty, depth + 1)
            board[n_r][n_c]='.'
        else:
            for i in range(4):
                if dir==i:
                    continue
                n_r, n_c = row + direct[i][0], col + direct[i][1]
                if n_r < 0 or n_c < 0 or n_r > n - 1 or n_c > m - 1:
                    continue
                if board[n_r][n_c] == '*':
                    continue

                board[n_r][n_c] = '*'
                dfs(n_r, n_c, i, level + 1, total_empty, depth + 1)
                board[n_r][n_c] = '.'

def get_total_empty(board):
    empty_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                empty_cnt += 1
    return empty_cnt


while True:
    answer = sys.maxsize
    try:
        n, m = map(int, sys.stdin.readline().split())
        board = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
        total_empty_cnt = get_total_empty(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    board[i][j] = '*'
                    dfs(i, j, -1, 0, total_empty_cnt, 1)
                    board[i][j] = '.'

        print(f'Case {test_case}: {answer if answer < sys.maxsize else -1}')
        test_case += 1
    except ValueError:
        break
