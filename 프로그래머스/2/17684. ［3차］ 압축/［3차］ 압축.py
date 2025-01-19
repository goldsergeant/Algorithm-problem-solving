import string

def get_default_dict():
    dict = {}
    for ch in string.ascii_uppercase:
        dict[ch] = ord(ch) - 64
    return dict
def solution(msg):
    answer = []
    dict=get_default_dict()

    left=0
    right=0
    while right<len(msg):
        while right<len(msg) and msg[left:right+1] in dict:
            right+=1
        answer.append(dict[msg[left:right]])
        dict[msg[left:right+1]]=len(dict)+1
        left=right

    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))