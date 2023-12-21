import sys


def get_total_digit(st: str):
    total = 0
    for char in st:
        if char.isdigit():
            total += int(char)

    return total


N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
arr.sort(key=lambda x: (len(x),get_total_digit(x),x))
for e in arr:
    print(e)