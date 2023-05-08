import sys

N=input()
if '0' not in N:
    print(-1)

else:
    num=0
    for i in range(len(N)):
        num+=int(N[i])

    if num%3==0:
        print(''.join(sorted(N,reverse=True)))
    else:
        print(-1)
