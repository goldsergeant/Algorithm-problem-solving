import sys

n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
apples = list(int(sys.stdin.readline()) for _ in range(j))
answer = 0
left = 1
right = m
for apple in apples:
    if left <= apple <= right:
        continue
    elif apple < left:
        answer += (left - apple)
        right -= (left - apple)
        left= apple
    elif apple > right:
        answer += (apple - right)
        left += (apple - right)
        right = apple

print(answer)
