s = input()
stack = []
prior = dict()
prior['*'] = 1
prior['/'] = 1
prior['+'] = 2
prior['-'] = 2
prior['('] = 3
for char in s:
    if char.isalpha():
        print(char, end='')
    else:
        if char == '*' or char == '/' or char == '+' or char == '-':
            while stack and prior[char] >= prior[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(char)
        elif char=='(':
            stack.append(char)

        elif char == ')':
            k=stack.pop()
            while k!='(':
                print(k,end='')
                k=stack.pop()
while stack:
    if len(stack) >= 2:
        opt2, opt1 = stack.pop(), stack.pop(),
        if prior[opt1] <= prior[opt2]:
            print(opt1, end='')
            print(opt2, end='')
        else:
            print(opt2, end='')
            print(opt1, end='')
    else:
        print(stack.pop(), end='')
