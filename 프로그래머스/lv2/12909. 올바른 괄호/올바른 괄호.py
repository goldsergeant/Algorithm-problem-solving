import collections
def solution(s):
    if s[0]!='(' or s[-1]!=')' or s.count('(') !=s.count(')'):
        return False
    stack=[]
    for char in s:
        if char=='(':
            stack.append('(')
        elif char==')':
            if len(stack)==0:
                return False
            stack.pop()
    return True