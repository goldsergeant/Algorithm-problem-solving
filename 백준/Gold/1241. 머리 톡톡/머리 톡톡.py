import sys

N=int(sys.stdin.readline())
check=[0 for _ in range(1000000 + 1)]
numbers=[]
for _ in range(N):
    num=int(sys.stdin.readline())
    check[num]+=1
    numbers.append(num)

for num in numbers:
    k=1
    answer=0
    while k*k<=num:
        if num%k==0:
            if k*k !=num:
                answer+=check[k]+check[num//k]
            else:
                answer+=check[k]
        k+=1

    print(answer-1)