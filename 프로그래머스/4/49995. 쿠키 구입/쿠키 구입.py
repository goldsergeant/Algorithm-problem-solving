def solution(cookie):
    answer = 0

    for m in range(1,len(cookie)):
        first,second=cookie[m-1],cookie[m]
        f_idx,s_idx=m-1,m
        while f_idx>=0 and s_idx<=len(cookie)-1:
            if first==second:
                answer=max(answer,first)
                if first>0:
                    f_idx-=1
                    first+=cookie[f_idx]
                elif second<len(cookie)-1:
                    s_idx+=1
                    second+=cookie[s_idx]
            elif first>second:
                if s_idx==len(cookie)-1:
                    break
                s_idx+=1
                second+=cookie[s_idx]
            else:
                if f_idx==0:
                    break
                f_idx-=1
                first+=cookie[f_idx]
    return answer

