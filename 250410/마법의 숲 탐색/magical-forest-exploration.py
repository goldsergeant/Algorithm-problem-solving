import collections
import copy

EXIT_IS_NORTH = 0
EXIT_IS_EAST = 1
EXIT_IS_SOUTH = 2
EXIT_IS_WEST = 3
golem_exit_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
golem_move_dir = [(1, 0), (0, -1), (0, 1)]

BOARD_EMPTY = 0
BOARD_EXIT = 1
BOARD_GOLEM = 2


def get_golem_points(center_r, center_c):  # 골렘의 위치들을 구하는 함수
    return [(center_r, center_c), (center_r - 1, center_c), (center_r, center_c - 1), (center_r + 1, center_c),
            (center_r, center_c + 1)]


def is_top_out_golem(center_r, center_c):  # 골렘이 위쪽에 걸터있을때
    if center_r - 1 < 3:
        return True
    return False


def place_golem(center_r, center_c, exit_state, golem_id):
    points = get_golem_points(center_r, center_c)
    for r, c in points:
        board[r][c] = BOARD_GOLEM
        golem_num_board[r][c] = golem_id

    if exit_state == EXIT_IS_NORTH:
        board[center_r - 1][center_c] = BOARD_EXIT
    elif exit_state == EXIT_IS_EAST:
        board[center_r][center_c + 1] = BOARD_EXIT
    elif exit_state == EXIT_IS_WEST:
        board[center_r][center_c - 1] = BOARD_EXIT
    elif exit_state == EXIT_IS_SOUTH:
        board[center_r+1][center_c] = BOARD_EXIT


def can_move_south(center_r, center_c):
    need_check_points = [(center_r + 1, center_c - 1), (center_r + 1, center_c + 1), (center_r + 2, center_c)]
    for r, c in need_check_points:
        if r >= R or board[r][c] != BOARD_EMPTY:
            return False
    return True


def can_move_west(center_r, center_c):
    first_need_check_points = [(center_r, center_c - 2), (center_r - 1, center_c - 1), (center_r + 1, center_c - 1)]
    second_need_check_points = [(center_r + 1, center_c - 2), (center_r + 2, center_c - 1)]
    for r, c in first_need_check_points:
        if r >= R or c < 0 or board[r][c] != BOARD_EMPTY:
            return False

    for r, c in second_need_check_points:
        if r >= R or c < 0 or board[r][c] != BOARD_EMPTY:
            return False

    return True


def can_move_east(center_r, center_c):
    first_need_check_points = [(center_r - 1, center_c + 1), (center_r, center_c + 2), (center_r + 1, center_c + 1)]
    second_need_check_points = [(center_r + 2, center_c + 1), (center_r + 1, center_c + 2)]
    for r, c in first_need_check_points:
        if r >= R or c >= C or board[r][c] != BOARD_EMPTY:
            return False

    for r, c in second_need_check_points:
        if r >= R or c >= C or board[r][c] != BOARD_EMPTY:
            return False
    return True


def move_golem_south(center_r, center_c, golem_id):
    have_to_move_points = get_golem_points(center_r, center_c)

    remove_points = [(center_r - 1, center_c), (center_r, center_c - 1), (center_r, center_c + 1)]
    for r, c in have_to_move_points:
        golem_num_board[r][c] = 0

    for r, c in have_to_move_points:
        board[r + 1][c] = BOARD_GOLEM
        golem_num_board[r + 1][c] = golem_id

    tmp_center_r,tmp_center_c=center_r+1,center_c
    if cur_exit_state== EXIT_IS_NORTH:
        board[tmp_center_r-1][tmp_center_c]=BOARD_EXIT
    elif cur_exit_state==EXIT_IS_SOUTH:
        board[tmp_center_r+1][tmp_center_c]=BOARD_EXIT
    elif cur_exit_state==EXIT_IS_WEST:
        board[tmp_center_r][tmp_center_c-1]=BOARD_EXIT
    elif cur_exit_state==EXIT_IS_EAST:
        board[tmp_center_r][tmp_center_c+1]=BOARD_EXIT

    for r, c in remove_points:
        board[r][c] = BOARD_EMPTY


def move_golem_west(center_r, center_c, exit_state, golem_id):
    global cur_exit_state

    have_to_move_points = get_golem_points(center_r, center_c)
    remove_points = [(center_r, center_c), (center_r - 1, center_c), (center_r, center_c + 1)]
    for r, c in have_to_move_points:
        golem_num_board[r][c] = 0
    for r, c in have_to_move_points:
        board[r + 1][c - 1] = BOARD_GOLEM
        golem_num_board[r + 1][c - 1] = golem_id

    tmp_center_r, tmp_center_c = center_r + 1, center_c - 1
    if exit_state == EXIT_IS_NORTH:  # 출구가 반시계방향으로 바뀜
        board[tmp_center_r][tmp_center_c - 1] = BOARD_EXIT
        cur_exit_state = EXIT_IS_WEST
    elif exit_state == EXIT_IS_EAST:
        board[tmp_center_r - 1][tmp_center_c] = BOARD_EXIT
        cur_exit_state = EXIT_IS_NORTH
    elif exit_state == EXIT_IS_WEST:
        board[tmp_center_r + 1][tmp_center_c] = BOARD_EXIT
        cur_exit_state = EXIT_IS_SOUTH
    elif exit_state == EXIT_IS_SOUTH:
        board[tmp_center_r][tmp_center_c + 1] = BOARD_EXIT
        cur_exit_state = EXIT_IS_EAST

    for r, c in remove_points:
        board[r][c] = BOARD_EMPTY


def move_golem_east(center_r, center_c, exit_state, golem_id):
    global cur_exit_state, board

    have_to_move_points = get_golem_points(center_r, center_c)
    remove_points = [(center_r, center_c), (center_r, center_c - 1), (center_r - 1, center_c)]
    for r, c in have_to_move_points:
        golem_num_board[r][c] = 0

    for r, c in have_to_move_points:
        board[r + 1][c + 1] = BOARD_GOLEM
        golem_num_board[r + 1][c + 1] = golem_id

    tmp_center_r, tmp_center_c = center_r + 1, center_c + 1
    if exit_state == EXIT_IS_NORTH:  # 출구가 시계방향으로 바뀜
        board[tmp_center_r][tmp_center_c + 1] = BOARD_EXIT
        cur_exit_state = EXIT_IS_EAST
    elif exit_state == EXIT_IS_EAST:
        board[tmp_center_r + 1][tmp_center_c] = BOARD_EXIT
        cur_exit_state = EXIT_IS_SOUTH
    elif exit_state == EXIT_IS_WEST:
        board[tmp_center_r - 1][tmp_center_c] = BOARD_EXIT
        cur_exit_state = EXIT_IS_NORTH
    elif exit_state == EXIT_IS_SOUTH:
        board[tmp_center_r][tmp_center_c - 1] = BOARD_EXIT
        cur_exit_state = EXIT_IS_WEST

    for r,c in remove_points:
        board[r][c]=BOARD_EMPTY

def elf_bfs(s_r, s_c):
    q = collections.deque([(s_r, s_c)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    last_r = s_r
    while q:
        r, c = q.popleft()
        last_r = max(r, last_r)
        for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 3 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == BOARD_EMPTY:
                continue

            if golem_num_board[nr][nc] == golem_num_board[r][c]:
                visited[nr][nc] = True
                q.append((nr, nc))
            else:
                if board[r][c] != BOARD_EXIT:
                    continue

                visited[nr][nc] = True
                q.append((nr, nc))

    return last_r


def clear_board():
    global board, golem_num_board
    board = [[BOARD_EMPTY for _ in range(C)] for _ in range(R)]
    golem_num_board = [[0 for _ in range(C)] for _ in range(R)]


R, C, K = map(int, input().split())
R += 3
board = [[BOARD_EMPTY for _ in range(C)] for _ in range(R)]  # 실제로 보드는 2열부터 시작한다고 가정
golem_num_board = [[0 for _ in range(C)] for _ in range(R)]
answer = 0
for golem_id in range(K):
    s_c, d = map(int, input().split())
    cur_exit_state = d
    s_c -= 1
    center_r, center_c = 1, s_c
    place_golem(center_r, center_c, cur_exit_state, golem_id)

    while True:
        is_gone = False
        if can_move_south(center_r, center_c):
            move_golem_south(center_r,center_c,golem_id)
            center_r += 1
            is_gone = True
        elif can_move_west(center_r, center_c):
            move_golem_west(center_r, center_c, cur_exit_state, golem_id)
            center_r += 1
            center_c -= 1
            is_gone = True
        elif can_move_east(center_r, center_c):
            move_golem_east(center_r, center_c, cur_exit_state, golem_id)
            center_r += 1
            center_c += 1
            is_gone = True

        if not is_gone:
            if is_top_out_golem(center_r, center_c):
                clear_board()
            else:
                last_r = elf_bfs(center_r, center_c)
                answer += last_r - 2
            break

print(answer)
# 마지막에 행 계산할떄 -2 해줘야함
