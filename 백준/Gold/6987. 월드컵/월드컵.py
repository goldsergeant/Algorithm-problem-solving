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

    if tmp_arr[home][n_win] > 0 and tmp_arr[away][n_lose] > 0:  # home이 이겼을때
        tmp_arr[home][n_win], tmp_arr[away][n_lose] = tmp_arr[home][n_win] - 1, tmp_arr[away][n_lose] - 1
        dfs(home, away + 1)
        tmp_arr[home][n_win], tmp_arr[away][n_lose] = tmp_arr[home][n_win] + 1, tmp_arr[away][n_lose] + 1

    if tmp_arr[home][n_draw] > 0 and tmp_arr[away][n_draw] > 0: # home이 비겼을때
        tmp_arr[home][n_draw], tmp_arr[away][n_draw] = tmp_arr[home][n_draw] - 1, tmp_arr[away][n_draw] - 1
        dfs(home, away + 1)
        tmp_arr[home][n_draw], tmp_arr[away][n_draw] = tmp_arr[home][n_draw] + 1, tmp_arr[away][n_draw] + 1

    if tmp_arr[home][n_lose] > 0 and tmp_arr[away][n_win] > 0: # home 이 졌을때
        tmp_arr[home][n_lose], tmp_arr[away][n_win] = tmp_arr[home][n_lose] - 1, tmp_arr[away][n_win] - 1
        dfs(home, away + 1)
        tmp_arr[home][n_lose], tmp_arr[away][n_win] = tmp_arr[home][n_lose] + 1, tmp_arr[away][n_win] + 1

for _ in range(4):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp_arr = []
    for i in range(6):
        tmp_arr.append([arr[i * 3], arr[i * 3 + n_draw], arr[i * 3 + n_lose]])
    is_possible = False
    dfs(0,1)
    print(1 if is_possible else 0)
