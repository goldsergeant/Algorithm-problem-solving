import collections
import sys

test_case = 1
dirs = [(0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    q = collections.deque([(0, 1)])
    dp = [[sys.maxsize] * 3 for _ in range(N)]
    dp[0][1] = arr[0][1]
    while q:
        y, x = q.popleft()

        for dir in dirs:
            d_y, d_x = dir
            n_y, n_x = y + d_y, x + d_x
            if n_y < 0 or n_y > N - 1 or n_x < 0 or n_x >= 3:
                continue
            if dp[n_y][n_x] > dp[y][x] + arr[n_y][n_x]:
                dp[n_y][n_x] = dp[y][x] + arr[n_y][n_x]
                q.append((n_y, n_x))

    print(f'{test_case}. {dp[N - 1][1]}')

    test_case += 1
