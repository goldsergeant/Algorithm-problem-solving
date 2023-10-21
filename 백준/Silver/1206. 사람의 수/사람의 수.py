import sys

n=int(sys.stdin.readline())
averages=[]
for _ in range(n):
    averages.append(int(sys.stdin.readline().split('.')[1]))

def check(cnt_people:int,averages:list):
    for avg in averages:
        left=0
        right=10*cnt_people
        is_possible = False
        while left<=right:
            sum_score=(left+right)//2
            cur_avg = (sum_score*1000)//cnt_people

            if cur_avg==avg:
                is_possible=True
                break

            elif cur_avg>avg:
                right=sum_score-1
            elif cur_avg<avg:
                left=sum_score+1

        if not is_possible:
            return False

    return True

for i in range(1,1001):
    if check(i,averages):
        print(i)
        break