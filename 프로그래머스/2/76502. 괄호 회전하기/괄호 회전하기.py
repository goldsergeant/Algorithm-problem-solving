import collections


def solution(s):
    answer = 0
    s = collections.deque(s)

    for rotate_cnt in range(len(s)):
        if rotate_cnt>0:
            s.rotate(-1)
        stack = []
        possible = True
        for ch in s:
            if ch in ['[', '{', '(']:
                stack.append(ch)
            else:
                if not stack:
                    possible = False
                    break
                if stack[-1] + ch in ('[]', '{}', '()'):
                    stack.pop()
                else:
                    possible = False
        if stack:
            possible = False
        if possible:
            answer+=1

    return answer


print(solution("}]()[{"))
