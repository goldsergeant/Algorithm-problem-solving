import itertools
import collections
from bisect import bisect_left,bisect_right

def get_avg(arr):
    total=0
    for n in arr:
        total+=n
    return total/len(arr)

def solution(dice):
    def dfs(idx,total,values,case):
        if idx==len(dice)//2:
            values.append(total)
            return
        for i in range(6):
            dfs(idx+1,total+dice[case[idx]][i],values,case)
    
    case_dict=collections.defaultdict(list)
    a_win_cnt_dict=collections.defaultdict(int)
    for case in itertools.combinations(range(len(dice)),len(dice)//2):
        values=[]
        dfs(0,0,values,case)
        case_dict[case]=sorted(values)
    
    for a_case in case_dict.keys():
        b_case=tuple(filter(lambda x: x not in a_case,range(len(dice))))
        a_numbers=case_dict[a_case]
        b_numbers=case_dict[b_case]
        
        for n in a_numbers:
            a_win_cnt_dict[a_case]+=bisect_left(b_numbers,n)
    max_item = sorted(a_win_cnt_dict.items(), key=lambda x: x[1], reverse=True)[0]
    return list(map(lambda x: x + 1, max_item[0]))