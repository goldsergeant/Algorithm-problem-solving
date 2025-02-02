import collections


def solution(number, k):
    stack=[]
    chance=k
    for ch in number:
        if not stack:
            stack.append(ch)
            continue
        while stack and chance>0 and ch>stack[-1]:
            stack.pop()
            chance-=1
        stack.append(ch)
    return ''.join(stack[:len(number)-k])