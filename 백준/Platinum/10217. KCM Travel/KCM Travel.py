import sys
import math
 
def solve():
  n, m, k = map(int, sys.stdin.readline().rstrip().split())
  table = [[] for _ in range(n+1)]
  for _ in range(k):
    u, v, c, d = map(int, sys.stdin.readline().rstrip().split())
    table[u].append((v, c, d))
  status = [[math.inf]*(m+1) for _ in range(n+1)]
  status[1][0] = 0
  for money in range(m+1):
    for vertex in range(1, n+1):
      if status[vertex][money] != math.inf:
        for v, c, d in table[vertex]:
          if money + c <= m:
            status[v][money+c]=min(status[v][money+c], status[vertex][money]+d)
  rst = min(status[n])
  if rst == math.inf:
    print("Poor KCM")
  else:
    print(rst)
 
t = int(input())
for _ in range(t):
  solve()