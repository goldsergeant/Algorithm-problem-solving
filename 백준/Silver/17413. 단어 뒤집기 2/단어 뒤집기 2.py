s = input()
answer = ''
i = 0
while i < len(s):
    if s[i] == '<':
        while s[i] != '>':
            answer += s[i]
            i += 1
        answer += s[i]
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        answer += ''.join(reversed(s[start:i]))
    else:
        answer+=s[i]
        i += 1

print(answer)
