import collections
import sys

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int, sys.stdin.readline().split())))

start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))
start[0] -= 1
start[1] -= 1
end[0] -= 1
end[1] -= 1
q = collections.deque()
q.appendleft((start[0], start[1], start[2], 0))
visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
visited[start[0]][start[1]][start[2]-1]=True

while q:
    row, col, dir, command_cnt = q.pop()
    if row == end[0] and col == end[1] and dir==end[2]:
        print(command_cnt)
        continue

    for move in [1, 2, 3]:
        if dir == 1:
            if col + move > n - 1 or board[row][col + move] == 1:
                break
            if not visited[row][col+move][dir-1]:
                visited[row][col + move][dir-1] = True
                q.appendleft((row, col + move, dir, command_cnt + 1))
        elif dir == 2:
            if col - move < 0 or board[row][col - move] == 1:
                break
            if not visited[row][col - move][dir-1]:
                q.appendleft((row, col - move, dir, command_cnt + 1))
                visited[row][col - move][dir-1] = True
        elif dir == 3:
            if row + move > m - 1 or board[row + move][col] == 1:
                break
            if not visited[row + move][col][dir-1]:
                q.appendleft((row + move, col, dir, command_cnt + 1))
                visited[row + move][col][dir-1] = True
        elif dir == 4:
            if row - move < 0 or board[row - move][col] == 1:
                break
            if not visited[row - move][col][dir-1]:
                q.appendleft((row - move, col, dir, command_cnt + 1))
                visited[row - move][col][dir-1] = True

    if dir == 1 or dir == 2:
        if not visited[row][col][3-1]:
            visited[row][col][3-1]=True
            q.appendleft((row, col, 3, command_cnt + 1))
        if not visited[row][col][4-1]:
            visited[row][col][4-1]=True
            q.appendleft((row, col, 4, command_cnt + 1))

    elif dir == 3 or dir == 4:
        if not visited[row][col][1-1]:
            visited[row][col][1-1]=True
            q.appendleft((row, col, 1,  command_cnt + 1))
        if not visited[row][col][2-1]:
            visited[row][col][2-1]=True
            q.appendleft((row, col, 2, command_cnt + 1))

