import collections
import sys

n=int(input())
queue=collections.deque()
for _ in range(n):
    s=sys.stdin.readline().strip()
    if 'push' in s:
        num=s.split()[1]
        queue.append(num)
    elif s == 'pop':
        print(queue.popleft() if len(queue)>0 else -1)

    elif s=='front':
        print(queue[0] if len(queue)>0 else -1)

    elif s=='back':
        print(queue[-1] if len(queue)>0 else -1)

    elif s=='size':
        print(len(queue))

    elif s=='empty':
        print(1 if len(queue)==0 else 0)