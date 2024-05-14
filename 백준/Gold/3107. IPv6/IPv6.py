import sys

address=sys.stdin.readline().rstrip()
remove_set = {''}

if '::' in address:
    temp=address.replace('::',':').split(':')
    temp=[i for i in temp if i not in remove_set]
    cnt=len(temp)
    st='0:'*(8-cnt)
    if address.find('::')>0:
        st=':'+st
    address=address.replace('::',st)

answer_arr=address.split(':')
answer_arr=[i for i in answer_arr if i not in remove_set]
print(':'.join(map(lambda x:x.zfill(4),answer_arr)))