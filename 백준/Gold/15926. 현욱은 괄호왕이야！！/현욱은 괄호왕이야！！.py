import sys

N = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()
answer=0
stack=[-1]
check_idx=[]
for idx,char in enumerate(st):
    if char=='(':
        stack.append(idx)
    else:
        stack.pop()
        if stack:
            answer=max(answer, idx-stack[-1])
        else:
            stack.append(idx)

print(answer)