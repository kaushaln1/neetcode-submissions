class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for n in nums :
            if hashmap[n]== 1 : 
                return True
            else:
                hashmap[n] +=1
        return False


        