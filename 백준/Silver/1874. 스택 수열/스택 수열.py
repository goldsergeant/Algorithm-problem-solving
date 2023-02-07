n=int(input())
stack=[0]
stack_opt=[]
cur_num=1
for i in range(n):
    num=int(input())
    if num not in stack and cur_num>num:
        print('NO')
        exit()

    while stack[-1]<num:
        stack.append(cur_num)
        stack_opt.append('+')
        cur_num+=1

    while stack[-1]>num and num in stack:
        stack.pop()
        stack_opt.append('-')

    if stack[-1]==num:
        stack.pop()
        stack_opt.append('-')


for opt in stack_opt:
    print(opt)