class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged=[]
        for i in sorted(intervals):
            if merged and merged[-1][1]>=i[0]:
                merged[-1][1]=max(merged[-1][1],i[1])
            else:
                merged+=i,
        return merged