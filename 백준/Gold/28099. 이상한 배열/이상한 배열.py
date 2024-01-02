import collections
import sys

T = int(sys.stdin.readline())


def solve(arr):
    counter = collections.Counter(arr)
    stack = []
    for i in range(len(arr)):
        if stack and stack[-1] < arr[i]:
            return False

        elif stack and stack[-1] == arr[i]:
            stack.pop()

        if counter[arr[i]] >= 2:
            stack.append(arr[i])
            counter[arr[i]] -= 1

    return True


for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print('Yes' if solve(arr) else 'No')
