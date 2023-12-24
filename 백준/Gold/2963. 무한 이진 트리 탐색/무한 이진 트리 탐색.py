import sys
sys.setrecursionlimit(100000)
commands = sys.stdin.readline().rstrip()

node=1
cnt=1
for char in commands:
    if char=='L':
        node*=2
    elif char=='R':
        node=2*node+cnt
    elif char=='*':
        node=5*node+cnt
        cnt*=3

print(node)
