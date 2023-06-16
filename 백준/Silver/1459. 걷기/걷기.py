X,Y,W,S=map(int,input().split())

cost1=(X+Y)*W
cost2=max(X,Y)*S if (X+Y)%2==0 else (max(X,Y)-1)*S+W
cost3=min(X,Y)*S+abs(X-Y)*W
        
print(min(cost1,cost2,cost3))