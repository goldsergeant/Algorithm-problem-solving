import collections

n=int(input())
stack=collections.deque()
for i in range(n):
    num=int(input())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
