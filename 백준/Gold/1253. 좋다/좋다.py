import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = 0

def binary_search(i):
    left = 0
    while left == i:
        left += 1

    right = N - 1
    while right == i:
        right -= 1

    target = numbers[i]

    while left < right:
        cur_target = numbers[left] + numbers[right]
        if cur_target < target:
            idx = left
            while numbers[idx] == numbers[left] or idx == i:
                idx += 1
                if idx>N-1:
                    return False
            left = idx
        elif cur_target > target:
            idx = right
            while numbers[idx] == numbers[right] or idx == i:
                idx -= 1
                if idx == -1:
                    return False
            right = idx
        else:
            return True

    return False

for i in range(N):
    if binary_search(i):
        answer+=1


print(answer)
