import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
stacks=[[] for _ in range(4)]

for num in numbers:
    tmp=sys.maxsize
    idx=-1
    for i in range(4):
        stack=stacks[i]
        if stack and stack[-1]<num and tmp>num-stack[-1]:
            idx=i
            tmp=num-stack[-1]

    if idx==-1:
        flag=False
        for stack in stacks:
            if not stack:
                stack.append(num)
                flag=True
                break
        if not flag:
            print('NO')
            exit()
    else:
        stacks[idx].append(num)



print('YES')