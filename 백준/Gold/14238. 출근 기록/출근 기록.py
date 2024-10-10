import sys
from functools import cache
st = sys.stdin.readline().rstrip()
answer = ['' for _ in range(len(st))]
# visited = [[[[[False for _ in range(3 + 1)] for _ in range(3 + 1)] for _ in range(st.count('C') + 1)] for _ in
#             range(st.count('B') + 1)] for _ in range(st.count('A') + 1)]  ## [a][b][c][prev_prev][prev]

@cache
def dfs(idx,a,b,c,prev_prev,prev):
    if idx==len(st):
        print(''.join(answer))
        exit()

    if a>0:
        answer[idx]='A'
        dfs(idx+1,a-1,b,c,prev,'A')
        answer[idx]=''

    if b>0 and prev!='B':
        answer[idx]='B'
        dfs(idx+1,a,b-1,c,prev,'B')
        answer[idx]=''

    if c>0 and prev!='C' and prev_prev!='C':
        answer[idx]='C'
        dfs(idx+1,a,b,c-1,prev,'C')
        answer[idx]=''

dfs(0,st.count('A'),st.count('B'),st.count('C'),'A','A')
print(-1)