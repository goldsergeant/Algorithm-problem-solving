def solution(s):
    answer = []
    s=s[1:len(s)-1]
    numbers=[]
    visited=[False for _ in range(100000+1)]

    stack=[]
    tmp_nums=[]
    for text in sorted(s.split('}'),key=len):
        if text=='':
            continue
        for ch in text+'}':
            if ch =='{':
                stack.append(ch)
            elif ch == '}':
                n=int(''.join(tmp_nums))
                if not visited[n]:
                    visited[n]=True
                    numbers.append(n)
                tmp_nums.clear()
                stack.pop()
            elif ch.isdigit():
                tmp_nums.append(ch)
            elif ch==',':
                if stack:
                    n=int(''.join(tmp_nums))
                    if not visited[n]:
                        visited[n]=True
                        numbers.append(n)
                    tmp_nums.clear()
                else:
                    continue


    return numbers