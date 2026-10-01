class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #2 pass hashmap
        index ={}

        for i, n in enumerate(nums):
            index[n] = i
        

        for i, n in enumerate(nums):
            diff = target-n
            if diff in index and i!=index[diff]:
                return [i , index[diff]]
                
        



        