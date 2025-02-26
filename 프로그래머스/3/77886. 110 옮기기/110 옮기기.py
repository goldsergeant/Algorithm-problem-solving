def solution(s):
    answer = []
    for string in s:
        check = [True for _ in range(len(string))]
        tmp = []
        cnt = 0
        stack = []
        for i in range(len(string)):
            while len(stack) >= 3 and string[stack[-3]] + string[stack[-2]] + string[stack[-1]] == '110':
                three, two, one = stack.pop(), stack.pop(), stack.pop()
                cnt += 1
                check[one] = check[two] = check[three] = False
            stack.append(i)
        while len(stack) >= 3 and string[stack[-3]] + string[stack[-2]] + string[stack[-1]] == '110':
            three, two, one = stack.pop(), stack.pop(), stack.pop()
            cnt += 1
            check[one] = check[two] = check[three] = False

        for i in range(len(string)):
            if check[i]:
                tmp.append(string[i])

        tmp=''.join(tmp)
        last_zero_idx=-1
        for i in range(len(tmp)-1,-1,-1):
            if tmp[i]=='0':
                last_zero_idx=i
                break
                
        if last_zero_idx==-1:
            answer.append('110'*cnt+tmp)
        else:
            answer.append(tmp[:last_zero_idx+1]+'110'*cnt+tmp[last_zero_idx+1:])
    return answer


print(solution(["01111010"]))
print(solution(["1110","100111100","0111111010"]))