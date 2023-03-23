n=int(input())
s=input()
num_list=[]
stack=[]
for _ in range(n):
    num_list.append(float(input()))

for char in s:
    if char.isalpha():
        stack.append(num_list[ord(char.lower())-97])
    else:
        num2,num1=stack.pop(),stack.pop(),
        stack.append(eval(str(num1)+char+str(num2)))

print('%.2f' %stack[0])
