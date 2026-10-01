class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        for i, num in enumerate(nums):
            prod = 1
            for j , n in enumerate(nums):
                if  i !=j:
                    if n ==0:
                        prod =0 
                        break
                    prod*=n 
            
            ans.append(prod)


        return ans

        