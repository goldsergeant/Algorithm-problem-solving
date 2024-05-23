import sys

P,M=map(int,sys.stdin.readline().split())
rooms=[]
for _ in range(P):
    level,name=sys.stdin.readline().split()
    level=int(level)
    if not rooms:
        rooms.append([(level,name)])
    else:
        is_in_exist_room=False
        for i in range(len(rooms)):
            if rooms[i][0][0]-10<=level<=rooms[i][0][0]+10 and len(rooms[i])<M:
                rooms[i].append((level,name))
                is_in_exist_room=True
                break

        if not is_in_exist_room:
            rooms.append([(level,name)])

for room in rooms:
    if len(room)==M:
        print('Started!')
    else:
        print('Waiting!')

    for level,name in sorted(room,key=lambda x:x[1]):
        print(level,name)
