import collections
def solution(s):
    stack=collections.deque()
    for char in s:
        if stack and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)
    return 1 if len(stack)==0 else 0