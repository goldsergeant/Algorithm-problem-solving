def solution(n):
    global answer
    def dfs(open_cnt,close_cnt):
        global answer
        if open_cnt==0 and close_cnt==0:
            answer+=1
            # print('ho')
            return
        
        if open_cnt>0:
            dfs(open_cnt-1,close_cnt)
        if open_cnt<close_cnt:
            dfs(open_cnt,close_cnt-1)
            
    answer = 0
    dfs(n-1,n)
    return answer