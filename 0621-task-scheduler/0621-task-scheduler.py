class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        result=0
        
        while True:
            sub_count=0
            
            for task,_ in counter.most_common(n+1):
                result+=1
                sub_count+=1
                
                counter.subtract(task)
                counter+=Counter()
                
            if not counter:
                break
            result+=n-sub_count+1
        return result