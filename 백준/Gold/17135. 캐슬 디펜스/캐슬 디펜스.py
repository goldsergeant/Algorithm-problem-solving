import copy
import heapq
import itertools
import sys

n, m, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] + [[0 for _ in range(m)]]
answer=0

def get_distance(r1, c1, r2, c2):
    return abs(r2 - r1) + abs(c2 - c1)


def get_attackable_enemy(board, archery_position, distance):
    enemy_positions=[]
    for i in reversed(range(max(0,n - distance), n)):
        for j in range(m):
            if board[i][j] == 1 and get_distance(archery_position[0], archery_position[1], i, j) <= distance:
                enemy_positions.append((i,j))
    if len(enemy_positions)>=2:
        enemy_positions.sort(key=lambda x:(get_distance(archery_position[0],archery_position[1],x[0],x[1]),x[1]))
    return enemy_positions[0] if enemy_positions else None


def forward_enemy(board):
    for i in reversed(range(1,n)):
        board[i] = board[i - 1]
    board[0]=[0]*m


for archery_cols in itertools.combinations(range(m), 3):
    archery_positions = [(n, archery_cols[i]) for i in range(3)]
    new_board=copy.deepcopy(board)
    tmp=0
    for _ in range(n):
        enemy_positions=set()
        for archery_position in archery_positions:
            position=get_attackable_enemy(new_board, archery_position,d)
            if position is not None:
                enemy_positions.add(get_attackable_enemy(new_board, archery_position,d))
        for enemy_position in enemy_positions:
            if new_board[enemy_position[0]][enemy_position[1]]==1:
                new_board[enemy_position[0]][enemy_position[1]]=0
                tmp+=1
        forward_enemy(new_board)
    answer=max(answer,tmp)

print(answer)