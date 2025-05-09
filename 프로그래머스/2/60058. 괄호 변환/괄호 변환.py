import collections

def solution(p):
    def is_right_string(string):
        stack=[]
        for ch in string:
            if ch=='(':
                stack.append('(')
            else:
                if not stack:
                    return False
                stack.pop()
                
        return len(stack)==0
    
    def is_balanced_string(string):
        counter=collections.Counter(string)
        return counter['(']==counter[')']
    
    def convert_string(string):
        tmp=[]
        for ch in string:
            tmp.append('(' if ch==')' else ')')
            
        return ''.join(tmp)
    
    def dfs(string):
        if string=='':
            return ''
        for i in range(1,len(string),2):
            u=string[:i+1]
            v=string[i+1:]
            if is_right_string(u):
                return u+dfs(v)
            elif is_balanced_string(u):
                return '('+dfs(v)+')'+convert_string(u[1:len(u)-1])
    return dfs(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))