def solution(sticker):
    if len(sticker)==1:
        return sticker[0]
    sticker1=sticker[:]
    sticker2=[sticker[-1]]+sticker[:len(sticker)-2]
    dp1=[0 for _ in range(len(sticker)-1)]
    dp2=[0 for _ in range(len(sticker)-1)]
    
    dp1[0]=sticker1[0]
    dp2[0]=sticker2[0]
    
    for i in range(1,len(dp1)):
        if i-2>=0:
            dp1[i]=max(dp1[i-1],dp1[i-2]+sticker1[i])
            dp2[i]=max(dp2[i-1],dp2[i-2]+sticker2[i])
        else:
            dp1[i]=max(dp1[i-1],sticker1[i])
            dp2[i]=max(dp2[i-1],sticker2[i])
    return max(dp1[-1],dp2[-1])