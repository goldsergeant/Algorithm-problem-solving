import collections
import sys

st1=collections.deque(sys.stdin.readline().strip())
st2=collections.deque()
n=int(sys.stdin.readline().strip())
for _ in range(n):
    command=list(sys.stdin.readline().strip())
    if 'P' == command[0]:
        st1.append(command[2])
    if 'L' == command[0]:
        if st1:
            st2.appendleft(st1.pop())
    if 'D' == command[0]:
        if st2:
            st1.append(st2.popleft())

    if 'B' == command[0]:
        if st1:
            st1.pop()

print(''.join(st1+st2))