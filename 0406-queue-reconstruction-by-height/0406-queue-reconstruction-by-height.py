class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[]
        people.sort(key=lambda x:(-x[0],x[1]))
        for p in people:
            result.insert(p[1],(p[0],p[1]))
        return result