import collections
import math

N, K, R = map(int, input().split())
cows = set()
roads= set()

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    roads.add(tuple(sorted([(r1, c1), (r2, c2)])))

for _ in range(K):
    r, c = map(int, input().split())
    cows.add((r, c))

meet_cows_without_roads_cnt=0
for s_r, s_c in cows:
    q = collections.deque([(s_r, s_c)])
    visited=set()
    visited.add((s_r, s_c))

    while q:
        r, c = q.popleft()
        if (s_r, s_c) != (r, c) and (r, c) in cows:
            meet_cows_without_roads_cnt+=1

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N:
                if (nr,nc) in visited:
                    continue
                if tuple(sorted([(r,c),(nr,nc)])) in roads:
                    continue

                visited.add((nr,nc))
                q.append((nr, nc))

# print(meet_cows_without_roads)
total_pair_count=math.comb(K,2)
print(total_pair_count - meet_cows_without_roads_cnt//2)
