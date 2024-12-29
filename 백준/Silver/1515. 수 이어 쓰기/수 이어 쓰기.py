import collections
import sys


st=collections.deque(list(sys.stdin.readline().strip()))

n=1
answer=0
while len(st):
    tmp=str(n)
    for ch in tmp:
        if len(st) and ch==st[0]:
            st.popleft()

    answer=n
    n+=1

print(answer)