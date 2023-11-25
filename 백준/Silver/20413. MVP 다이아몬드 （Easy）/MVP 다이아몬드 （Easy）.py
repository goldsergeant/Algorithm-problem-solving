import sys

n=int(sys.stdin.readline())
silver_to_dia=list(map(int,sys.stdin.readline().split()))
level_dict=dict()
level_dict['S']=silver_to_dia[0]
level_dict['G']=silver_to_dia[1]
level_dict['P']=silver_to_dia[2]
level_dict['D']=silver_to_dia[3]
levels=sys.stdin.readline().rstrip()

paid_money_arr=[]
for level in levels:
    if level=='B':
        if paid_money_arr:
            paid_money_arr.append(level_dict['S']-paid_money_arr[-1]-1)
        else:
            paid_money_arr.append(level_dict['S']-1)
    elif level=='S':
        if paid_money_arr:
            paid_money_arr.append(level_dict['G']-paid_money_arr[-1]-1)
        else:
            paid_money_arr.append(level_dict['G']-1)
    elif level == 'G':
        if paid_money_arr:
            paid_money_arr.append(level_dict['P']-paid_money_arr[-1]-1)
        else:
            paid_money_arr.append(level_dict['P']-1)
    elif level=='P':
        if paid_money_arr:
            paid_money_arr.append(level_dict['D']-paid_money_arr[-1]-1)
        else:
            paid_money_arr.append(level_dict['D']-1)
    elif level == 'D':
            paid_money_arr.append(level_dict['D'])


print(sum(paid_money_arr))