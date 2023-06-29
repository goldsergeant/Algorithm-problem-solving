n = int(input())
minus_men = []
plus_men = []
minus_women = []
plus_women = []
tmp = list(map(int, input().split()))
answer = 0

for i in tmp:
    if i < 0:
        minus_men.append(i)
    else:
        plus_men.append(i)

tmp = list(map(int, input().split()))

for i in tmp:
    if i < 0:
        minus_women.append(i)
    else:
        plus_women.append(i)

minus_men.sort(reverse=True)
minus_women.sort(reverse=True)
plus_men.sort()
plus_women.sort()

minus_men_point = 0
plus_women_point = 0

while minus_men_point < len(minus_men) and plus_women_point < len(plus_women):
    if abs(minus_men[minus_men_point]) > abs(plus_women[plus_women_point]):
        minus_men_point += 1
        answer += 1
        plus_women_point+=1
    else:
        minus_men_point += 1

plus_men_point = 0
minus_women_point = 0

while plus_men_point < len(plus_men) and minus_women_point < len(minus_women):
    if abs(plus_men[plus_men_point]) < abs(minus_women[minus_women_point]):
        plus_men_point += 1
        answer += 1
        minus_women_point+=1
    else:
        minus_women_point += 1

print(answer)
