import copy

EMPTY = 0
EXIT = -1
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
participants = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
exit_r, exit_c = map(lambda x: int(x) - 1, input().split())
participant_board = [[0 for _ in range(N)] for _ in range(N)]
for r, c in participants:
    participant_board[r][c] += 1
board[exit_r][exit_c] = EXIT


def get_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def is_out_area(r, c):
    if r < 0 or c < 0 or r >= N or c >= N:
        return True
    return False


def is_in_participant():
    for i in range(N):
        for j in range(N):
            if participant_board[i][j] > 0:
                return True
    return False


def move_participants():
    global participant_board,total_participant_move

    tmp_participant_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if participant_board[i][j] > 0:
                cur_dist = get_dist(i, j, exit_r, exit_c)
                flag = False
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
                    nr, nc = i + dr, j + dc
                    if is_out_area(nr, nc):
                        continue
                    if board[nr][nc] not in (EMPTY, EXIT):
                        continue

                    n_dist = get_dist(nr, nc, exit_r, exit_c)
                    if n_dist >= cur_dist:
                        continue
                    tmp_participant_board[nr][nc] += participant_board[i][j]
                    total_participant_move+=participant_board[i][j]
                    if board[nr][nc]==EXIT:
                        tmp_participant_board[nr][nc]=0
                    flag = True
                    break
                if not flag:
                    tmp_participant_board[i][j] += participant_board[i][j]
    participant_board = tmp_participant_board


def get_smallest_square():
    square_arr = []
    for top_left_r in range(N):
        for top_left_c in range(N):
            bottom_right_r = top_left_r + 1
            bottom_right_c = top_left_c + 1
            while not is_out_area(bottom_right_r, bottom_right_c):
                is_have_participant = False
                is_have_exit = False
                for i in range(top_left_r, bottom_right_r + 1):
                    for j in range(top_left_c, bottom_right_c + 1):
                        if (i, j) == (exit_r, exit_c):
                            is_have_exit = True
                        if participant_board[i][j] > 0:
                            is_have_participant = True

                if is_have_participant and is_have_exit:
                    size = bottom_right_r - top_left_r
                    square_arr.append((size, top_left_r, top_left_c, bottom_right_r, bottom_right_c))
                    break

                bottom_right_r += 1
                bottom_right_c += 1

    square_arr.sort(key=lambda x: (x[0], x[1], x[2]))
    return square_arr[0][1:]


def rotate_right_90(top_left_r, top_left_c, bottom_right_r, bottom_right_c):
    global board, participant_board, exit_r, exit_c
    tmp_board = copy.deepcopy(board)
    tmp_participant_board = copy.deepcopy(participant_board)
    tmp_r = top_left_r
    tmp_c = bottom_right_c
    for r in range(top_left_r, bottom_right_r + 1):
        for c in range(top_left_c, bottom_right_c + 1):
            if board[r][c] > EMPTY:
                tmp_board[tmp_r][tmp_c] = board[r][c] - 1
            else:
                tmp_board[tmp_r][tmp_c] = board[r][c]
            tmp_participant_board[tmp_r][tmp_c] = participant_board[r][c]
            if tmp_board[tmp_r][tmp_c] == EXIT:
                exit_r, exit_c = tmp_r, tmp_c
            tmp_r += 1
            if tmp_r > bottom_right_r:
                tmp_r = top_left_r
                tmp_c -= 1

    board = tmp_board
    participant_board = tmp_participant_board


total_participant_move = 0
for _ in range(K):
    if not is_in_participant():
        break
    move_participants()
    top_left_r, top_left_c, bottom_right_r, bottom_right_c = get_smallest_square()
    rotate_right_90(top_left_r, top_left_c, bottom_right_r, bottom_right_c)

print(total_participant_move)
print(exit_r + 1, exit_c + 1)
