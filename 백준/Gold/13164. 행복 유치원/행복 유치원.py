import sys

N,K=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
diff_arr=sorted([(numbers[i+1]-numbers[i]) for i in range(len(numbers)-1)],reverse=True)
print(sum(diff_arr[K-1:]))