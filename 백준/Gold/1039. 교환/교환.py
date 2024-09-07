import collections
import sys

N, K = sys.stdin.readline().split()
N = list(N)
K = int(K)
# while K >= len(N):
#     K -= 2
# if K==0:
#     if len(N)==2 and N[-1]=='0':
#         print(-1)
#         exit()
#     if len(N)==1:
#         print(-1)
#         exit()

q = collections.deque([(N.copy(), 0)])
answer = -1
visited = set()
visited.add((''.join(N), 0))

while q:
    arr, cnt = q.popleft()
    if cnt == K:
        answer = max(answer, int(''.join(arr)))
        continue

    for i in range(len(N)):
        for j in range(i + 1, len(N)):
            if arr[j] == '0' and i == 0:
                continue
            arr[i], arr[j] = arr[j], arr[i]
            if (''.join(arr), cnt + 1) not in visited:
                q.append((arr.copy(), cnt + 1))
                visited.add((''.join(arr), cnt + 1))
            arr[i], arr[j] = arr[j], arr[i]

print(answer)