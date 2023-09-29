import collections
import sys

n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
num_range=range(-1000,1001)
can_a=collections.defaultdict(list)
possible_num=set([i for i in num_range])
answer=set()

if n==1:
    print('A')
    exit()

for i in range(1,n):
    pre,cur=numbers[i-1],numbers[i]

    for a in num_range:
        if a not in possible_num:
            continue

        if can_a[a]==[]:
            can_a[a].append(cur-pre*a)
        else:
            if pre*a+can_a[a][0]!=cur:
                possible_num.remove(a)

if not possible_num:
    print('B')
else:
    for a in possible_num:
        answer.add(numbers[-1]*a+can_a[a][0])

    print('A' if len(answer)>1 else answer.pop())