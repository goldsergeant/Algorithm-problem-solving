import collections

str = input()
answer = 0
stack = collections.deque()
num=1
for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')
        num*=2
    elif str[i] == ')':
        if len(stack)>0 and stack[-1] == '(':
            stack.pop()
            if str[i-1]=='(':
                answer+=num
            num//=2
        else:
            print(0)
            exit()
    elif str[i] == '[':
        stack.append('[')
        num*=3
    elif str[i] == ']':
        if len(stack)>0 and stack[-1] == '[':
            stack.pop()
            if str[i - 1] == '[':
                answer += num
            num //= 3
        else:
            print(0)
            exit()
print(answer) if len(stack)==0 else print(0)
