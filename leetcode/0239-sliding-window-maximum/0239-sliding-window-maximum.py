class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        maxheap=[]
        
        for i in range(k):
            heapq.heappush(maxheap,(-nums[i],i))
            
        ans.append(-maxheap[0][0])
        
        for i in range(k,len(nums)):
            heapq.heappush(maxheap,(-nums[i],i))
            while maxheap and maxheap[0][1]<i-k+1:
                heapq.heappop(maxheap)
            ans.append(-maxheap[0][0])
        return ans