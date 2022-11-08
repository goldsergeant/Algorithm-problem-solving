def solution(answers):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    first=second=third=0
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            first+=1
        if answers[i]==two[i%8]:
            second+=1
        if answers[i]==three[i%10]:
            third+=1
    m=max(first,second,third)
    answer=[(1,first),(2,second),(3,third)]
    return [i[0] for i in answer if i[1]==m]