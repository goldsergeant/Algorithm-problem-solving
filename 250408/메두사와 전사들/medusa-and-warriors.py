import collections
import sys

medusa_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
warrior_first_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
warrior_second_dir = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우상하
medusa_sight_dir = [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)], [(-1, -1), (0, -1), (1, -1)],
                    [(-1, 1), (0, 1), (1, 1)]]  # 상 하 좌 우


def in_check(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


def get_medusa_route(s_r, s_c):
    q = collections.deque([(s_r, s_c, 0, [])])
    medusa_visited = [[False for _ in range(N)] for _ in range(N)]
    medusa_visited[s_r][s_c] = True

    while q:
        r, c, cnt, route = q.popleft()
        if (r, c) == (e_r, e_c):
            return route
        for dr, dc in medusa_dir:
            nr, nc = r + dr, c + dc
            if not in_check(nr, nc) or medusa_visited[nr][nc] or board[nr][nc] == 1:
                continue

            q.append((nr, nc, cnt + 1, route + [(nr, nc)]))
            medusa_visited[nr][nc] = True

    return None


def see_medusa(r, c):
    global total_stone_warriors, is_warrior_stopped

    def check_straight_impossible_see(s_r,s_c):
        cur_r,cur_c = s_r + straight_dr, s_c + straight_dc
        while in_check(cur_r, cur_c):
            if (s_r, s_c) != (cur_r, cur_c) and visited[cur_r][cur_c]:
                break
            visited[cur_r][cur_c] = True
            cur_r, cur_c = cur_r + straight_dr, cur_c + straight_dc

    def check_impossible_see(s_r, s_c, dr, dc):
        can_see = True
        cur_r, cur_c = s_r+dr, s_c+dc
        while in_check(cur_r, cur_c):
            if (s_r, s_c) != (cur_r, cur_c) and visited[cur_r][cur_c]:
                break
            visited[cur_r][cur_c] = True
            if warrior_points[(cur_r, cur_c)] > 0 and can_see:
                tmp_warrior_stopped[cur_r][cur_c]=can_see
                can_see = False
                check_straight_impossible_see(cur_r,cur_c)
            else:
                tmp_warrior_stopped[cur_r][cur_c] = can_see
            cur_r, cur_c = cur_r + dr, cur_c + dc

    is_warrior_stopped = [[False for _ in range(N)] for _ in range(N)]
    sight_arr = []
    straight_dr,straight_dc=0,0

    for i in range(len(medusa_sight_dir)):
        tmp_warrior_stopped = [[False for _ in range(N)] for _ in range(N)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        left_idx = 0
        mid_idx = 1
        right_idx = 2
        tmp_r, tmp_c = r, c
        straight_dr,straight_dc=medusa_sight_dir[i][mid_idx][0], medusa_sight_dir[i][mid_idx][1]
        while in_check(tmp_r, tmp_c):
            check_impossible_see(tmp_r, tmp_c, medusa_sight_dir[i][mid_idx][0],
                                 medusa_sight_dir[i][mid_idx][1])  # 바라보는 방향
            check_impossible_see(tmp_r, tmp_c, medusa_sight_dir[i][left_idx][0],
                                 medusa_sight_dir[i][left_idx][1])  # 왼쪽 대각선
            check_impossible_see(tmp_r, tmp_c, medusa_sight_dir[i][right_idx][0],
                                 medusa_sight_dir[i][right_idx][1])  # 오른쪽 대각선
            tmp_r, tmp_c = tmp_r + medusa_sight_dir[i][mid_idx][0], tmp_c + medusa_sight_dir[i][mid_idx][1]

        stop_warrior_cnt = 0
        for i in range(N):
            for j in range(N):
                if tmp_warrior_stopped[i][j]:
                    stop_warrior_cnt += warrior_points[(i, j)]

        sight_arr.append([stop_warrior_cnt, i, tmp_warrior_stopped])


    sight_arr.sort(key=lambda x: (-x[0], x[1]))


    for i in range(N):
        for j in range(N):
            if sight_arr[0][2][i][j]:
                total_stone_warriors += warrior_points[(i, j)]

    tmp_warrior_stopped = sight_arr[0][2]
    for i in range(N):
        for j in range(N):
            is_warrior_stopped[i][j] = tmp_warrior_stopped[i][j]

    is_warrior_stopped[r][c]=False

def attack_warrior(medusa_r, medusa_c):  # 메두사가 전사를
    if (medusa_r, medusa_c) in warrior_points:
        warrior_points.pop((medusa_r, medusa_c))


def move_warrior(medusa_r, medusa_c):
    global warrior_points, total_warrior_move_distance
    new_warrior_points = collections.defaultdict(int)

    for r, c in warrior_points.keys():
        if warrior_points[(r, c)] == 0:
            continue
        if is_warrior_stopped[r][c]:
            new_warrior_points[(r, c)] += warrior_points[(r, c)]
            continue
        distance_arr = []
        origin_dist = abs(r - medusa_r) + abs(c - medusa_c)
        warrior_cnt = warrior_points[(r, c)]
        for i in range(4):
            nr, nc = r + warrior_first_dir[i][0], c + warrior_first_dir[i][1]
            if not in_check(nr, nc):
                continue
            dist = abs(nr - medusa_r) + abs(nc - medusa_c)
            if is_warrior_stopped[nr][nc] or dist >= origin_dist:
                continue
            distance_arr.append((dist, i, nr, nc))

        if not distance_arr:
            new_warrior_points[(r,c)]+=warrior_cnt
            continue
        distance_arr.sort()
        nr, nc = distance_arr[0][2], distance_arr[0][3]
        total_warrior_move_distance += warrior_cnt

        if (nr, nc) == (medusa_r, medusa_c):
            attack_medusa(nr, nc, warrior_cnt)
            continue

        distance_arr.clear()
        n_dist = abs(nr - medusa_r) + abs(nc - medusa_c)
        for i in range(4):
            nnr, nnc = nr + warrior_second_dir[i][0], nc + warrior_second_dir[i][1]
            if not in_check(nnr, nnc) or is_warrior_stopped[nnr][nnc]:
                continue
            nn_dist = abs(nnr - medusa_r) + abs(nnc - medusa_c)
            if nn_dist >= n_dist:
                continue
            distance_arr.append((nn_dist, i, nnr, nnc))

        if not distance_arr:
            new_warrior_points[(nr,nc)]+=warrior_cnt
            continue

        distance_arr.sort()
        nnr, nnc = distance_arr[0][2], distance_arr[0][3]
        total_warrior_move_distance += warrior_cnt
        if (nnr, nnc) == (medusa_r, medusa_c):
            attack_medusa(nnr, nnc, warrior_cnt)
            continue
        new_warrior_points[(nnr,nnc)]+=warrior_cnt
    warrior_points = new_warrior_points


def attack_medusa(r, c, cnt):
    global total_attack_medusa_warriors
    total_attack_medusa_warriors += cnt


N, M = map(int, input().split())
s_r, s_c, e_r, e_c = map(int, input().split())
warriors = list(map(int, input().split()))
warrior_points = collections.defaultdict(int)
is_warrior_stopped = [[False for _ in range(N)] for _ in range(N)]
answer = []
medusa_route = []

for i in range(0, len(warriors), 2):
    r,c = warriors[i], warriors[i + 1]
    warrior_points[(r, c)] += 1

board = [list(map(int, input().split())) for _ in range(N)]
medusa_route = get_medusa_route(s_r, s_c)
if medusa_route is None:
    print(-1)
    exit()

for medusa_r, medusa_c in medusa_route:
    if (medusa_r, medusa_c) == (e_r, e_c):
        print(0)
    else:
        total_warrior_move_distance = 0
        total_stone_warriors = 0
        total_attack_medusa_warriors = 0
        attack_warrior(medusa_r, medusa_c)
        see_medusa(medusa_r, medusa_c)
        move_warrior(medusa_r, medusa_c)
        print(total_warrior_move_distance, total_stone_warriors, total_attack_medusa_warriors)

for i in range(len(answer)):
    print(*answer[i])
