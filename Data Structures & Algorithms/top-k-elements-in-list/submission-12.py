class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
        
        ans = []
        for key, value in map.items():
            ans.append([value,key])

        ans.sort()
        
        print(ans)
        res =[]
        while len(res)<k:
            res.append(ans.pop()[1])

        return res
