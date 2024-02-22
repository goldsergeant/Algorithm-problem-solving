import sys

EMPTY = '.'
FIRST = 'X'
SECOND = 'O'
win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
finish_arr = set()
board=list('.........')

def get_board(i,j):
    return board[i*3+j]
def set_board(i,j,value):
    board[i*3+j]=value

def finish_check():
    for i in range(len(win)):
        if board[win[i][0]]!=EMPTY and board[win[i][0]]==board[win[i][1]] and board[win[i][1]]==board[win[i][2]]:
            return True
    return False

def dfs(turn,depth):
    if finish_check() or depth==9:
        finish_arr.add(''.join(board))
        return

    for i in range(3):
        for j in range(3):
            if get_board(i,j)==EMPTY:
                set_board(i,j,turn)
                if turn==FIRST:
                    dfs(SECOND,depth+1)
                elif turn==SECOND:
                    dfs(FIRST,depth+1)
                set_board(i,j,EMPTY)
dfs(FIRST,0)


while True:
    arr = sys.stdin.readline().rstrip()
    if arr == 'end':
        break
    print('valid' if arr in finish_arr else 'invalid')

