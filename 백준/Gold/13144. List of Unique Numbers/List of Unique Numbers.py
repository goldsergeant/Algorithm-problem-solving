import collections
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
snapshot=set()
right = 0
for left in range(N):
    while right < N and numbers[right] not in snapshot:
        snapshot.add(numbers[right])
        right += 1
    answer += (right - left)
    snapshot.remove(numbers[left])
print(answer)