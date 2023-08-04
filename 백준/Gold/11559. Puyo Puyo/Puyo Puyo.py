import sys

field = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
answer = 0

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def check():
    for line in field:
        if not all(i == '.' for i in line):
            return False

    return True


def dfs(row, col, puyo, visited_points):
    for i in range(4):
        n_row = row + dy[i]
        n_col = col + dx[i]
        if n_row < 0 or n_col < 0 or n_row >= 12 or n_col >= 6:
            continue
        if field[n_row][n_col] != puyo:
            continue
        if (n_row, n_col) in visited_points:
            continue

        visited_points.append((n_row, n_col))
        dfs(n_row, n_col, puyo, visited_points)


def gravity():
    for col in range(6):
        for row in range(10, -1, -1):
            if field[row][col] != '.':
                target_row = row
                for j in range(target_row + 1, 12):
                    if field[j][col] == '.':
                        target_row = j
                    else:
                        break

                field[row][col], field[target_row][col] = field[target_row][col], field[row][col]


while True:
    isCompleted = True
    for row in range(12):
        for col in range(6):
            if field[row][col] != '.':
                visited_points = []
                dfs(row, col, field[row][col], visited_points)
                if len(visited_points) >= 4:
                    isCompleted = False
                    for point in visited_points:
                        field[point[0]][point[1]] = '.'
    gravity()

    if isCompleted:
        break
    else:
        answer += 1

print(answer)
