import sys

index=1
while True:
    S=input()
    answer=0
    if '-' in S:
        break
    stack=[]

    for char in S:
        if char=='}' and stack and stack[-1]=='{':
            stack.pop()
        else:
            stack.append(char)

    while stack:
        s1=stack.pop()
        s2=stack.pop()
        if s1==s2:
            answer+=1
        else:
            answer+=2

    print('{}. {}'.format(index,answer))

    index+=1