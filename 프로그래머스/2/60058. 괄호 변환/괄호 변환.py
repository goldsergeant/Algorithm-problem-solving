def solution(p):
    def is_right(string):
        stack=[]
        for char in string:
            if char=='(':
                stack.append(char)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack)==0

    def dfs(string):
        if string=='':
            return ''

        left_cnt=0
        right_cnt=0
        idx=-1
        for char in string:
            idx+=1
            if char=='(':
                left_cnt+=1
            else:
                right_cnt+=1
            if left_cnt==right_cnt:
                break

        u=string[:idx+1]
        v=string[idx+1:] if idx<len(string)-1 else ''

        if not is_right(u):
            tmp=list(u[1:len(u)-1])
            for i in range(len(tmp)):
                if tmp[i]=='(':
                    tmp[i]=')'
                else:
                    tmp[i]='('

            return '('+dfs(v)+')'+''.join(tmp)
        else:
            return u+dfs(v)

    return dfs(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))