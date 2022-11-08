def solution(s):
    s_arr=s.split()
    for i in range(len(s_arr)):
        s_arr[i]=int(s_arr[i])
    answer=str(min(s_arr))+" "+str(max(s_arr))
    return answer