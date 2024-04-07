import sys

st=sys.stdin.readline().rstrip()
answer=0
k=0
p=0
for char in st:
    if char=='K':
        k+=1
        p=max(0,p-1)
    else:
        p+=1
        k=max(0,k-1)

    answer=max(answer,k,p)
print(answer)