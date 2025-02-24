def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack=[0]
    for i in range(1,len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
            idx=stack.pop()
            answer[idx]=numbers[i]
        stack.append(i)
            
    return answer