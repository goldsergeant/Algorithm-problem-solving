import collections
import sys

S, T = map(int, sys.stdin.readline().split())
answer = []

if S == T:
    print(0)
    exit()


def bfs():
    visited = set()
    visited.add(S)
    q = collections.deque([(S, '')])

    while q:
        num, st = q.popleft()
        if num == T:
            return st

        for next_opt in ['*', '+', '-', '/']:
            if next_opt == '*':
                if num * num <= T and num*num not in visited:
                    visited.add(num*num)
                    q.append((num * num, st + next_opt))
            elif next_opt == '+':
                if num + num <= T and num+num not in visited:
                    visited.add(num+num)
                    q.append((num + num, st + next_opt))
            elif next_opt == '-':
                if num - num >= 0 and num-num not in visited:
                    visited.add(num-num)
                    q.append((num - num, st + next_opt))
            elif next_opt == '/':
                if num != 0 and num//num not in visited:
                    visited.add(num//num)
                    q.append((num // num, st + next_opt))


print(bfs() or -1)
