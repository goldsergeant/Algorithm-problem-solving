import sys

n_win = 0
n_draw = 1
n_lose = 2


def dfs(home, away):
    global is_possible
    if away == 6:
        home += 1
        away = home + 1
    if home == 5:
        if tmp_arr == [[0, 0, 0] for _ in range(6)]:
            is_possible = True
        return

    for res1,res2 in ((n_win,n_lose),(n_draw,n_draw),(n_lose,n_win),):
        if tmp_arr[home][res1]>0 and tmp_arr[away][res2]>0:
            tmp_arr[home][res1],tmp_arr[away][res2]=tmp_arr[home][res1]-1,tmp_arr[away][res2]-1
            dfs(home,away+1)
            tmp_arr[home][res1], tmp_arr[away][res2] = tmp_arr[home][res1] + 1, tmp_arr[away][res2] + 1

for _ in range(4):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp_arr = []
    for i in range(6):
        tmp_arr.append([arr[i * 3], arr[i * 3 + n_draw], arr[i * 3 + n_lose]])
    is_possible = False
    dfs(0,1)
    print(1 if is_possible else 0)
