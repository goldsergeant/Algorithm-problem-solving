import sys

N=int(sys.stdin.readline())
stack=[]
cur = ''
for _ in range(N):
    command,arg,second = sys.stdin.readline().split()
    second=int(second)
    if command=='type':
        cur+=arg
        stack.append((second,cur))
    else:
        arg=int(arg)
        flag=False
        for i in range(len(stack)-1,-1,-1):
            if stack[i][0]<second-arg:
                cur=stack[i][1]
                stack.append((second,cur))
                flag=True
                break
        if not flag:
            cur=''
            stack.append((second,cur))

print(cur)