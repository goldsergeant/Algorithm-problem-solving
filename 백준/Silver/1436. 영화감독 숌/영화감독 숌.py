n=int(input())
num=666
flag=0
while True:
    if '666' in str(num):
        flag+=1
    if flag==n:
        print(num)
        break
    num+=1