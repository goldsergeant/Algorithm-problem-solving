import sys

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def check(l, r, t, b):
    temp = board[t][l]
    for row in range(t, b + 1):
        for col in range(l, r + 1):
            if temp != board[row][col]:
                return False

    return True


def dfs(l, r, t, b):
    if check(l, r, t, b):
        return board[t][l]

    hor_center = (l + r) // 2
    ver_center = (t + b) // 2
    temp = ['(']
    temp.append(dfs(l, hor_center, t, ver_center))
    temp.append(dfs(hor_center + 1, r, t, ver_center))
    temp.append(dfs(l, hor_center, ver_center + 1, b))
    temp.append(dfs(hor_center + 1, r, ver_center + 1, b))
    temp.append(')')
    return ''.join(temp)

print(dfs(0,N-1,0,N-1))
