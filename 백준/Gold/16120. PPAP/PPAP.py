import collections
import sys

string = list(sys.stdin.readline().rstrip())
stack = []

for char in string:
    stack.append(char)
    while len(stack) >= 4:
        if [stack[-4], stack[-3], stack[-2], stack[-1]] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('P')
        else:
            break

while len(stack) >= 4:
    if [stack[-4], stack[-3], stack[-2], stack[-1]] == ['P', 'P', 'A', 'P']:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append('P')
    else:
        break

if stack==['P']:
    print('PPAP')
else:
    print('NP')