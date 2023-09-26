import sys

st=sys.stdin.readline().rstrip()

total_a=st.count('a')
answer=sys.maxsize
for i in range(len(st)):
    tmp=[]
    for j in range(i,i+total_a):
        tmp.append(st[j%len(st)])
    answer=min(answer,tmp.count('b'))

print(answer)