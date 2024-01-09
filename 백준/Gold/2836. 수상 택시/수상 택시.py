import sys

N, M = map(int, sys.stdin.readline().split())
right_to_left = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        right_to_left.append((b, a))

right_to_left.sort()

converted_lines = []
for start, end in right_to_left:
    if not converted_lines:
        converted_lines.append((start, end))
        continue

    prev_start, prev_end = converted_lines[-1]
    if start <= prev_end:
        converted_lines.pop()
        converted_lines.append((prev_start, max(end, prev_end)))

    else:
        converted_lines.append((start, end))

total=sum([b-a for a,b in converted_lines])
print(M+total*2)
