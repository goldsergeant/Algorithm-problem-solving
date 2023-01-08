n=int(input())
def recur(n):
    if n==3:
        return ['***','* *','***']
    arr=recur(n//3)
    stars=[]
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)

    return stars
print('\n'.join(recur(n)))