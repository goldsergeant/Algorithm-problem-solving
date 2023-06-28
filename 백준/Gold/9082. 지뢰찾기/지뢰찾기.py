dx = [-1, 0, 1]

t = int(input())

def check_nearby_mine_exist(idx):
    for i in range(3):
        if arr[idx] == 0:
            break
        nx = dx[i] + idx
        if nx < 0 or nx > n - 1:
            continue
        if mines[nx] == '*':
            arr[idx] -= 1

def check_no_mines(idx):
    for i in range(3):
        nx=dx[i]+idx
        if nx < 0 or nx > n - 1:
            continue
        if mines[nx]!='*':
            check[nx]=2

def make_mine(idx):
    for i in range(3):
        nx=dx[i]+idx
        if nx < 0 or nx > n - 1:
            continue
        if check[nx]==0:
            check[nx]=1
        elif check[nx]==1 and mines[nx]=='#':
            mines[nx]='*'
            arr[idx]-=1
            if arr[idx]==0:
                check_no_mines(idx)
                break

for _ in range(t):
    n = int(input())
    arr = list(map(int, input()))
    mines = list(input())
    check=[0 for _ in range(n)]

    for i in range(n):
        check_nearby_mine_exist(i)
        if arr[i]==0:
            check_no_mines(i)
            continue
        make_mine(i)

    print(mines.count('*'))
