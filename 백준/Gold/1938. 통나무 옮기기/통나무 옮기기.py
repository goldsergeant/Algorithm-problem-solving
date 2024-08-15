import collections
import sys


def check_move_log(logs, dy, dx):
    for y, x in logs:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= N or nx >= N or board[ny][nx] == '1':
            return False
    return True


def check_rotate_logs(logs):
    center = logs[1]
    for i in range(center[0] - 1, center[0] + 2):
        for j in range(center[1] - 1, center[1] + 2):
            if i < 0 or j < 0 or i >= N or j >= N or board[i][j] == '1':
                return False
    return True


def move_logs(logs, dy, dx):
    moved_logs = []
    for y, x in logs:
        moved_logs.append((y + dy, x + dx))
    return sorted(moved_logs)


def rotate_logs(logs):
    center = logs[1]
    if logs[0][0] + 1 == logs[1][0]:  # 세로 방향인 통나무
        left = (center[0], center[1] - 1)
        right = (center[0], center[1] + 1)
        return [left, center, right]
    else:  # 가로 방향인 통나무
        top = (center[0] - 1, center[1])
        bottom = (center[0] + 1, center[1])
        return [top, center, bottom]


N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
log_points = []
end_points = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            log_points.append((i, j))
        elif board[i][j] == 'E':
            end_points.append((i, j))
end_points.sort()

q = collections.deque([(log_points.copy(), 0)])
visited = set()
while q:
    logs, cnt = q.popleft()
    logs.sort()

    if logs == end_points:
        print(cnt)
        exit()

    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        if check_move_log(logs, dy, dx):
            moved_logs = move_logs(logs, dy, dx)
            if tuple(moved_logs) not in visited:
                visited.add(tuple(moved_logs))
                q.append((moved_logs, cnt + 1))

    if check_rotate_logs(logs):
        rotated_logs = rotate_logs(logs)
        if tuple(rotated_logs) not in visited:
            visited.add(tuple(rotated_logs))
            q.append((rotated_logs, cnt + 1))

print(0)
