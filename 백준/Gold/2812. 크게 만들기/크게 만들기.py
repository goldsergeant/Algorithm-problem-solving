n,k=map(int,input().split())
num=list(input())
chance=0
stack=[num[0]]

for i in range(1,len(num)):
    if chance<k:
        while stack and stack[-1]<num[i] and chance<k:
            stack.pop()
            chance+=1

    stack.append(num[i])

while chance<k:
    stack.pop()
    chance+=1

print(''.join(stack))