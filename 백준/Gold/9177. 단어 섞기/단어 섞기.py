import collections
import sys

N = int(sys.stdin.readline())


def bfs():
    q = collections.deque([(0, 0, 0)])
    visited = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    visited[0][0] = True

    while q:
        a_idx, b_idx,c_idx = q.popleft()
        if c_idx==len(c):
            return True

        if len(a) > a_idx and a[a_idx] == c[c_idx] and not visited[a_idx + 1][b_idx]:
            visited[a_idx + 1][b_idx] = True
            q.append((a_idx + 1, b_idx,c_idx+1))

        if len(b) > b_idx and b[b_idx] == c[c_idx] and not visited[a_idx][b_idx + 1]:
            visited[a_idx][b_idx + 1] = True
            q.append((a_idx, b_idx + 1,c_idx+1,))

    return False


for t in range(1, N + 1):
    a, b, c = map(list, sys.stdin.readline().split())
    print(f'Data set {t}: yes') if bfs() else print(f'Data set {t}: no')
