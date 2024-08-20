import collections
import sys
START=0
END=50

def get_next(start,cur,go_cnt):
    if cur==END or go_cnt==0:
        return cur
    if cur==start and start in [10,20,30]:
        return get_next(start,graph[cur][1],go_cnt-1)

    return get_next(start,graph[cur][0],go_cnt-1)
def get_score(node):
    if node==11:
        return 13
    if node==13:
        return 16
    if node==15:
        return 19
    if node==21:
        return 22
    if node==23:
        return 24
    if node==31:
        return 28
    if node==33:
        return 27
    if node==35:
        return 26
    if node==41:
        return 30
    if node==43:
        return 35
    if node==END:
        return 0

    return node


graph=collections.defaultdict(list)
for i in range(0,40,2):
    graph[i].append(i+2)

graph[10].append(11)
graph[11].append(13)
graph[13].append(15)
graph[15].append(25)

graph[20].append(21)
graph[21].append(23)
graph[23].append(25)

graph[30].append(31)
graph[31].append(33)
graph[33].append(35)
graph[35].append(25)

graph[25].append(41)
graph[41].append(43)
graph[43].append(40)

graph[40].append(END)

dices=list(map(int,sys.stdin.readline().split()))
pieces=[START,START,START,START]
answer=0

def dfs(idx,score):
    global answer
    if idx==10:
        answer=max(score,answer)
        return

    for i in range(4):
        if pieces[i]==END:
            continue
        cur_piece=pieces[i]
        next_piece=get_next(pieces[i],pieces[i],dices[idx])
        if next_piece!=END and next_piece in pieces:
            continue

        pieces[i]=next_piece
        dfs(idx+1,score+get_score(next_piece))
        pieces[i]=cur_piece


dfs(0,0)
print(answer)