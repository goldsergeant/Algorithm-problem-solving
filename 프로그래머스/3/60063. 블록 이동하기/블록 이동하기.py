from collections import deque


def solution(board):
    N, M = len(board), len(board[0])

    def push_visited(r1, c1, r2, c2):
        visited.add(tuple(sorted([(r1, c1), (r2, c2)])))

    def check_visited(r1, c1, r2, c2):
        return tuple(sorted([(r1, c1), (r2, c2)])) in visited

    def push_queue(r1, c1, r2, c2, sec):
        q.append(tuple(sorted([(r1, c1), (r2, c2)])) + (sec,))

    def is_vertical(r1, c1, r2, c2):
        return r1+1==r2

    visited = set()

    q = deque([((0, 0), (0, 1), 0)])
    push_visited(0, 0, 0, 1)
    while q:
        point1, point2, sec = q.popleft()
        r1,c1 = point1
        r2,c2 = point2
        if (r1, c1) == (N - 1, M - 1) or (r2, c2) == (N - 1, M - 1):
            return sec

        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            nr1, nc1, nr2, nc2 = r1 + dr, c1 + dc, r2 + dr, c2 + dc
            if nr1 < 0 or nc1 < 0 or nr2 < 0 or nc2 < 0 or nr1 >= N or nc1 >= M or nr2 >= N or nc2 >= M:
                continue
            if board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                continue
            if check_visited(nr1, nc1, nr2, nc2):
                continue

            push_queue(nr1, nc1, nr2, nc2, sec + 1)
            push_visited(nr1, nc1, nr2, nc2)

        if is_vertical(r1,c1,r2,c2):
            for dr, dc in (1, -1), (1, 1):  # 아래 축을 기준으로 위쪽이 움직일 때
                nr1,nc1=r1+dr,c1+dc
                if nr1<0 or nc1<0 or nr1>=N or nc1>=M:
                    continue
                if board[nr1][nc1]==1 or board[nr1-1][nc1]==1:
                    continue
                if check_visited(nr1, nc1, r2,c2):
                    continue
                push_queue(nr1,nc1,r2,c2,sec+1)
                push_visited(nr1,nc1,r2,c2)

            for dr,dc in (-1,-1),(-1,1): # 위쪽 축을 기준으로 아래쪽이 움직일 때
                nr2,nc2=r2+dr,c2+dc
                if nr2<0 or nc2<0 or nr2>=N or nc2>=M:
                    continue
                if board[nr2][nc2] == 1 or board[nr2 + 1][nc2] == 1:
                    continue
                if check_visited(r1,c1,nr2,nc2):
                    continue
                push_queue(r1,c1,nr2,nc2,sec+1)
                push_visited(r1,c1,nr2,nc2)

        else:
            for dr,dc in (-1,1),(1,1): #오른쪽 축을 기준으로 왼쪽이 움직일 때
                nr1,nc1=r1+dr,c1+dc
                if nr1<0 or nc1<0 or nr1>=N or nc1>=M:
                    continue
                if board[nr1][nc1]==1 or board[nr1][nc1-1]==1:
                    continue
                if check_visited(nr1, nc1, r2,c2):
                    continue
                push_queue(nr1,nc1,r2,c2,sec+1)
                push_visited(nr1,nc1,r2,c2)

            for dr,dc in (-1,-1),(1,-1): #왼쪽 축을 기준으로 오른쪽이 움직일 때
                nr2,nc2=r2+dr,c2+dc
                if nr2 < 0 or nc2 < 0 or nr2 >= N or nc2 >= M:
                    continue
                if board[nr2][nc2] == 1 or board[nr2][nc2 + 1] == 1:
                    continue
                if check_visited(r1,c1,nr2,nc2):
                    continue
                push_queue(r1,c1,nr2,nc2, sec + 1)
                push_visited(r1,c1,nr2,nc2)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))