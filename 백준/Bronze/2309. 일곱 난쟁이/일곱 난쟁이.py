arr=[]
def arrPrint(i,j):
    for k in range(9):
        if k!=i and k!=j:
            print(arr[k])

def checkArr(i,j):
    result=0
    for k in range(len(arr)):
        if k!=i and k!=j:
            result+=arr[k]
    return result
for i in range(9):
    arr.append(int(input()))
arr.sort()
for i in range(8):
    for j in range(i+1,9):
        if checkArr(i,j)==100:
            arrPrint(i,j)
            exit()