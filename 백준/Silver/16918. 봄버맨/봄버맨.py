import sys

EMPTY = '.'
BOMB = 'O'
R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
board = [list(map(lambda x: [x, 0], board[i])) for i in range(R)]
second = 0


def boom():
    bomb_points = []
    for i in range(R):
        for j in range(C):
            if board[i][j][0] == BOMB and board[i][j][1] >= 3:
                bomb_points.append((i, j))

    for y, x in bomb_points:
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny = y + dy
                nx = x + dx
                board[y][x]=[EMPTY,0]
                if 0 <= ny < R and 0 <= nx < C:
                    board[ny][nx] = [EMPTY, 0]



def plant_bomb():
    for i in range(R):
        for j in range(C):
            if board[i][j][0] == EMPTY:
                board[i][j] = [BOMB, 0]

def increase_second_bomb():
    for i in range(R):
        for j in range(C):
            if board[i][j][0]==BOMB:
                board[i][j][1]+=1


while second < N:
    second += 1
    increase_second_bomb()
    if second == 1:
        continue
    if second%2==0:
        plant_bomb()
    else:
        boom()

for arr in board:
    print(''.join(map(lambda x:x[0],arr)))
