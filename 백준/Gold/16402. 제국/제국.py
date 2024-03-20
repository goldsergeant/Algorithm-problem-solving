import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
parent = dict()


def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(winner, loser):
    p_winner = find(winner)
    p_loser = find(loser)
    if p_winner == p_loser:
        parent[loser] = winner
        parent[winner] = winner
    else:
        parent[p_loser] = p_winner


for _ in range(N):
    st = sys.stdin.readline().rstrip()
    parent[st] = st

for _ in range(M):
    one,two,w = sys.stdin.readline().rstrip().split(',')
    if w == '1':
        union(one, two)
    else:
        union(two, one)

answer = [key for key in parent.keys() if key==parent[key]]

print(len(answer))
for kingdom in sorted(answer):
    print(kingdom)
