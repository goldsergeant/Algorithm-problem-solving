import sys

N, M, L = map(int, sys.stdin.readline().split())
stations = [0, L]
if M != 0:
    stations = [0] + list(map(int, sys.stdin.readline().split())) + [L]

stations.sort()
left = 0
right = L
while left + 1 < right:
    mid = (left + right) // 2
    count = 0
    for i in range(1, len(stations)):
        if stations[i] - stations[i - 1] // mid > 0:
            count += (stations[i] - stations[i - 1] - 1) // mid

    if count > M:
        left = mid
    else:
        right = mid

print(right)
