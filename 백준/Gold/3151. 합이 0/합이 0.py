import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
skills = list(map(int, sys.stdin.readline().split()))
skills.sort()
answer = 0
for target_idx in range(N - 2):
    left = target_idx + 1
    right = N - 1
    target = -skills[target_idx]
    while left < right:
        mid = skills[left] + skills[right]
        if mid < target:
            left += 1
        elif mid > target:
            right -= 1
        else:
            if skills[left] == skills[right]:
                answer += right - left
            else:
                answer += right - bisect_left(skills, skills[right]) + 1
            left += 1
print(answer)
