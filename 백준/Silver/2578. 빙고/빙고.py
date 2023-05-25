import sys


def check(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                return


def bingo() -> bool:
    count = 0
    for row in range(5):  # 가로 검사
        if sum(board[row])==0:
            count+=1

    for col in range(5): # 세로 검사
        for row in range(5):
            if board[row][col]!=0:
                break
            if row==4:
                count+=1


    for idx in range(5):  # 왼쪽으로 누운 대각선 검사
        if board[idx][idx] != 0:
            break
        if idx == 4:
            count += 1

    for idx in range(5):  # 오른쪽으로 누운 대각선 검사
        if board[idx][4 - idx] != 0:
            break
        if idx == 4:
            count += 1

    if count >= 3:
        return True
    else:
        return False


board=[]
numbers=[]
for _ in range(5):
    board.append(list(map(int,sys.stdin.readline().split())))

for _ in range(5):
    numbers.append(list(map(int,sys.stdin.readline().split())))

idx=0

for i in range(5):
    for j in range(5):
        idx+=1
        check(numbers[i][j])
        if bingo():
            print(idx)
            exit()
