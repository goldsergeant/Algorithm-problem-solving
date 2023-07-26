import collections
import sys

n, m = map(int, input().split())
board = []
coins = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
answer = []


def is_coin_inside_of_board(row, col):
    if row < 0 or col < 0 or row > n - 1 or col > m - 1:
        return False
    return True


def bfs():
    queue = collections.deque()
    queue.appendleft((coins[0][0], coins[0][1], 0))  # y,x,total
    queue.appendleft((coins[1][0], coins[1][1], 0))  # y,x,total
    while queue:
        coin1 = queue.pop()
        coin2 = queue.pop()
        if (is_coin_inside_of_board(coin1[0], coin1[1]) and not is_coin_inside_of_board(coin2[0], coin2[1])) or (
                not is_coin_inside_of_board(coin1[0], coin1[1]) and is_coin_inside_of_board(coin2[0], coin2[1])):
            answer.append(coin1[2])
            continue
        if coin1[2] == 10:
            continue

        for i in range(4):
            move_coin1_y = coin1[0] + dy[i]
            move_coin1_x = coin1[1] + dx[i]
            move_coin2_y = coin2[0] + dy[i]
            move_coin2_x = coin2[1] + dx[i]
            if not is_coin_inside_of_board(move_coin1_y, move_coin1_x) and not is_coin_inside_of_board(move_coin2_y,
                                                                                                       move_coin2_x):
                continue

            if is_coin_inside_of_board(move_coin1_y, move_coin1_x):
                if board[move_coin1_y][move_coin1_x] == '#':
                    queue.appendleft((coin1[0], coin1[1], coin1[2] + 1))
                else:
                    queue.appendleft((move_coin1_y, move_coin1_x, coin1[2] + 1))
            else:
                queue.appendleft((move_coin1_y,move_coin1_x,coin1[2]+1))

            if is_coin_inside_of_board(move_coin2_y, move_coin2_x):
                if board[move_coin2_y][move_coin2_x] == '#':
                    queue.appendleft((coin2[0], coin2[1], coin2[2] + 1))
                else:
                    queue.appendleft((move_coin2_y, move_coin2_x, coin2[2] + 1))
            else:
                queue.appendleft((move_coin2_y,move_coin2_x,coin2[2]+1))


for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

for i in range(n):  # 동전 찾기
    for j in range(m):
        if board[i][j] == 'o':
            coins.append([i, j])

bfs()
print(min(answer) if answer else -1)
