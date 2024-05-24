import sys

def moo(total_len,mid_len,n):
    if n<=3:
        return 'moo'[n-1]

    left_len=(total_len-mid_len)//2

    if n<=left_len: #왼쪽
        return moo(left_len,mid_len-1,n)
    if n>left_len+mid_len: #오른쪽
        return moo(left_len,mid_len-1,n-left_len-mid_len)

    if n-left_len==1:
        return 'm'
    else:
        return 'o'


N=int(sys.stdin.readline())

total_len,n=3,0
while total_len<N:
    n+=1
    total_len=total_len*2+n+3

print(moo(total_len,n+3,N))