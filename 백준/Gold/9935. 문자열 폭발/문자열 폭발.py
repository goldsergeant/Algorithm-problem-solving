string = list(input())
target = input()
stack = []

for i in range(len(string)):
    stack.append(string[i])

    while len(stack) >= len(target) and ''.join(stack[-len(target):]) == target:
            for _ in range(len(target)):
                stack.pop()

print(''.join(stack) if stack else 'FRULA')