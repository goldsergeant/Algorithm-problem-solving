import collections
import math
import sys
sys.setrecursionlimit(100000)

def solution(enroll, referral, seller, amount):
    def divide_profit(person,money):
        parent_money=math.floor(money//10)
        my_money=money-parent_money
        profit[person]+=my_money
        if person!=parent[person] and parent_money>0:
            divide_profit(parent[person],parent_money)
            
    person_to_idx=dict()
    parent=[i for i in range(len(enroll))]
    profit=[0 for  _ in range(len(enroll))]
    for i in range(len(enroll)):
        person_to_idx[enroll[i]]=i
        if referral[i]!='-':
            referral_name=referral[i]
            parent[i]=person_to_idx[referral_name]
    
    for i in range(len(seller)):
        divide_profit(person_to_idx[seller[i]],amount[i]*100)
    
    return profit