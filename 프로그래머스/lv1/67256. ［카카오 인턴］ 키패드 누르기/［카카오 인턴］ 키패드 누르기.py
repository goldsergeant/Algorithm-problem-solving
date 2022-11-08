def solution(numbers, hand):
    dic={
        1:(1,1),
        2:(1,2),
        3:(1,3),
        4:(2,1),
        5:(2,2),
        6:(2,3),
        7:(3,1),
        8:(3,2),
        9:(3,3),
        0:(4,2)
    }
    result=''
    left,right=(4,1),(4,3)
    for num in numbers:
        if dic[num][1]==1:
            result+='L'
            left=dic[num]
        elif dic[num][1]==3:
            result+='R'
            right=dic[num]
        else:
            if abs(left[0]-dic[num][0])+abs(left[1]-dic[num][1])<abs(right[0]-dic[num][0])+abs(right[1]-dic[num][1]):
                result+='L'
                left=dic[num]
            elif abs(left[0]-dic[num][0])+abs(left[1]-dic[num][1])>abs(right[0]-dic[num][0])+abs(right[1]-dic[num][1]):
                result+='R'
                right=dic[num]
            else:
                if hand=='left':
                    result+='L'
                    left=dic[num]
                else:
                    result+='R'
                    right=dic[num]
    return result
    