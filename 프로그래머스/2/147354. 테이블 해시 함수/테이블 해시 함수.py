def solution(data, col, row_begin, row_end):
    s_i=[]
    data.sort(key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin-1,row_end):
        total=0
        for j in range(len(data[i])):
            total+=data[i][j]%(i+1)
        s_i.append(total)
        
    answer=s_i[0]
    for i in range(1,len(s_i)):
        answer=answer^s_i[i]
    return answer