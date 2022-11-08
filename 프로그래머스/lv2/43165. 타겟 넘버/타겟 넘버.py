def solution(numbers, target):
    answer = [0]
    def dfs(index,number,target,answer):
        if index==len(numbers)-1:
            if number==target:
                answer[0]+=1
            return
        dfs(index+1,number+numbers[index+1],target,answer)
        dfs(index+1,number-numbers[index+1],target,answer)
    dfs(-1,0,target,answer)
    return answer[0]