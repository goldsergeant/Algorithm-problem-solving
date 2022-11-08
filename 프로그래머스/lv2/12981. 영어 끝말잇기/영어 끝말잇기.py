def solution(n, words):
    answer=[0,0]
    check_list=[]
    words.insert(0,0);
    for i in range(1,len(words)):
        if words[i] in check_list or (i>1 and words[i][0]!=words[i-1][-1]):
            answer[1]=i//n+1
            if i%n==0:
                answer[1]-=1
            answer[0]=i%n
            if answer[0]==0:
                answer[0]=n
            break
        check_list.append(words[i])
    return answer