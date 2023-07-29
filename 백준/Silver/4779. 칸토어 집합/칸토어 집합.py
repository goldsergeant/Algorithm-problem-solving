import sys


def recur(st,start,size):
    if size==1:
        return st
    new_size=size//3

    for i in range(start+new_size,start+(2*new_size)):
        st[i]=' '

    recur(st,start,new_size)
    recur(st,start+(2*new_size),new_size)

    return st


while True:
    try:
        n=int(input())
        if n=='':
            break
        st=list('-'*(3**n))
        print(''.join(recur(st,0,len(st))))
    except EOFError:
        break