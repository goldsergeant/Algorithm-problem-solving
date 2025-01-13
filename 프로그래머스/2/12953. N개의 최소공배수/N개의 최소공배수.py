def solution(arr):
    num=max(arr)
    factor=num
    while True:
        if all(num%i==0 for i in arr):
            return num
        num+=factor
    
            