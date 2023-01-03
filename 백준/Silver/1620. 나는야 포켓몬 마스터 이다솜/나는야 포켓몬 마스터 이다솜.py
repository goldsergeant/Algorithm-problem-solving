n,m=map(int,input().split())
pokemons=dict()
pokemons2=dict()
index=1
for i in range(n):
    st=input()
    pokemons[index]=st
    pokemons2[st]=index
    index+=1

for i in range(m):
    temp=input()
    if temp.isnumeric():
        print(pokemons[int(temp)])
    else:
        print(pokemons2[temp])