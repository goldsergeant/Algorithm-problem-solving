import collections
import sys

n = int(input())
stack = collections.deque()
for _ in range(n):
    st = sys.stdin.readline().rstrip()
    if 'push' in st:
        stack.append(st.split()[1])
    elif st == 'top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    elif st == 'size':
        print(len(stack))
    elif st == "empty":
        print(1 if len(stack) == 0 else 0)
    elif st == 'pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
