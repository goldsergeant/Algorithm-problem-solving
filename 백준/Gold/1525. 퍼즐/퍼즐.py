import collections
import sys
from copy import deepcopy

def convert_2d_array_to_tuple(array):
    return tuple(sum(array, []))


board = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
visited = set()
answer = 0

q = collections.deque([board])
visited.add(convert_2d_array_to_tuple(board))
sorted_tup =tuple([i for i in range(1,9)]+[0])
while q:
    for _ in range(len(q)):
        cur_board = q.popleft()
        cur_tup = convert_2d_array_to_tuple(cur_board)
        if cur_tup == sorted_tup:
            print(answer)
            exit()

        empty_row,empty_col=0,0
        for i in range(3):
            for j in range(3):
                if cur_board[i][j]==0:
                    empty_row,empty_col=i,j
                    break

        for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]:
            ny,nx=empty_row+dy,empty_col+dx
            if ny<0 or nx<0 or ny>=3 or nx>=3:
                continue

            cur_board[empty_row][empty_col],cur_board[ny][nx]=cur_board[ny][nx],cur_board[empty_row][empty_col]
            next_tup=convert_2d_array_to_tuple(cur_board)
            if next_tup not in visited:
                visited.add(next_tup)
                q.append(deepcopy(cur_board))
            cur_board[empty_row][empty_col],cur_board[ny][nx]=cur_board[ny][nx],cur_board[empty_row][empty_col]

    answer+=1
print(-1)
