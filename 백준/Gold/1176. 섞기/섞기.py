import sys

N,K=map(int,sys.stdin.readline().split())
students=[int(sys.stdin.readline()) for _ in range(N)]
dp=[[0 for _ in range(1<<N)] for _ in range(N)] # 마지막 학생 키, 방문 비트

for i in range(N):
    dp[i][1<<i]=1

for cur_bit in range(1<<N):
    for student in range(N):
        student_bit=1<<student
        if not cur_bit&student_bit:
            continue
        for next_student in range(N):
            next_student_bit=1<<next_student
            if cur_bit&next_student_bit:
                continue
            if abs(students[student]-students[next_student])>K:
                n_bit=cur_bit|next_student_bit
                dp[next_student][n_bit]+=dp[student][cur_bit]

answer=0
for i in range(N):
    answer+=dp[i][(1<<N)-1]

print(answer)