def get_head(file):
    idx=0
    while idx<len(file) and not file[idx].isnumeric():
        idx+=1
    return file[:idx]

def get_number(file):
    left=0
    while left<len(file) and not file[left].isnumeric():
        left+=1
    right=left
    while right<len(file) and file[right].isnumeric():
        right+=1

    return int(file[left:right])

def solution(files):
    return sorted(files,key=lambda x:(get_head(x).lower(),get_number(x)))