class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        elements=[]
        for i in range(1,n+1):
            elements.append(i)
        return list(map(list,itertools.combinations(elements,k)))
            