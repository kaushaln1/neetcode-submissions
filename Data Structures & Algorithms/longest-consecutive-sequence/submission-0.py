class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap ={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] =1
        
        max = 0
        for key in hashmap.keys():
            if key-1 not in hashmap:
                localmax=1
                while (key+1) in hashmap:
                    localmax+=1
                    key+=1

                if localmax > max:
                    max = localmax


                
        return max

        