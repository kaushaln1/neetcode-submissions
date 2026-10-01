class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for n in nums:
            map[n]+=1
        
        startpoints = []

        for n in nums:
            if n-1 not in map:
                startpoints.append(n)
            
        print(startpoints)
        maxlen= 0 

        for st in startpoints:
            count= 1 
            while st+1 in map:
                st +=1
                count+=1

            
            if count > maxlen : 
                maxlen= count
            
        return maxlen
        