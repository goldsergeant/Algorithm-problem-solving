n=int(input())
answer_list=[0,1,2,3]
for i in range(4,n+1):
    answer_list.append(answer_list[i-2]+answer_list[i-1])

print(answer_list[n]%10007)