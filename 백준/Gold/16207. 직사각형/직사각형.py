import sys

N=int(sys.stdin.readline())
numbers=sorted(map(int,sys.stdin.readline().split()),reverse=True)
answer=0
stack1=[]
stack2=[]

for num in numbers:
    if not stack1:
        stack1.append(num)
        continue

    if num+1>=stack1[-1]:
        if not stack2:
            stack2.append(min(stack1[-1],num))
        else:
            answer+=min(stack1[-1],num)*stack2[-1]
            stack2.clear()
        stack1.clear()
    else:
        stack1.append(num)

print(answer)