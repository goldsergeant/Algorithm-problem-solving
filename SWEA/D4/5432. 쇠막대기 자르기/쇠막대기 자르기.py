def is_lazer(i):
    return st[i-1]=='(' and st[i]==')'

T=int(input())
for test_case in range(1,T+1):
    st=input()

    stack=[]
    answer=0

    for idx,val in enumerate(st):
        if not stack:
            stack.append(val)
            continue

        if val=='(':
            stack.append(val)
        else:
            if is_lazer(idx):
                stack.pop()
                answer+=len(stack)
            else:
                stack.pop()
                answer+=1

    print(f'#{test_case} {answer}')