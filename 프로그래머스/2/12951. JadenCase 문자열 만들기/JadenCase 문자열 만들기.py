def solution(s):
    answer = []
    is_first=True
    for i in range(len(s)):
        if s[i].isspace():
            answer.append(s[i])
            is_first=True
        else:
            if is_first:
                answer.append(s[i].upper())
                is_first=False
            else:
                answer.append(s[i].lower())
    return ''.join(answer)