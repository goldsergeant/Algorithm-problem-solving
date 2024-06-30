import collections
import sys

def connect(cur,next):
    next_list[cur]=next
    prev_list[next]=cur

N, M = map(int, sys.stdin.readline().split())
stations = [*map(int, sys.stdin.readline().split())]
next_list = [0 for _ in range(1000000+1)]
prev_list = [0 for _ in range(1000000+1)]
for i in range(len(stations)):
    cur, next = stations[i], stations[(i + 1) % len(stations)]
    connect(cur,next)

for _ in range(M):
    arr = sys.stdin.readline().split()
    command = arr[0]
    numbers = [*map(int, arr[1:])]
    if command == 'BN':
        cur, establish = numbers[0], numbers[1]
        next = next_list[cur]
        print(next)

        connect(establish,next)
        connect(cur,establish)

    elif command == 'BP':
        cur, establish = numbers[0], numbers[1]
        prev = prev_list[cur]
        print(prev)

        connect(prev,establish)
        connect(establish,cur)

    elif command == 'CN':
        cur = numbers[0]
        next = next_list[cur]
        print(next)
        next_next = next_list[next]
        connect(cur,next_next)
        next_list[next]=0
        prev_list[next]=0

    elif command == 'CP':
        cur = numbers[0]
        prev = prev_list[cur]
        print(prev)
        prev_prev = prev_list[prev]
        connect(prev_prev,cur)

        prev_list[prev]=0
        next_list[prev]=0