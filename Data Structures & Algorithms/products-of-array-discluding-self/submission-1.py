class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # ans = []
        # for i, num in enumerate(nums):
        #     prod = 1
        #     for j , n in enumerate(nums):
        #         if  i !=j:
        #             if n ==0:
        #                 prod =0 
        #                 break
        #             prod*=n 
            
        #     ans.append(prod)


        # return ans
        
        productfwd = []
        productback = []

        n= len(nums)
        prod=1
        productfwd.append(1)         
        for i in range(0,n-1):
            prod*=nums[i]
            productfwd.append(prod)

        # print (n, productfwd)
        prod =1 
        productback.append(1) 
        for i in range(n-1,0,-1):
            prod*=nums[i]
            # print(prod)
            productback.append(prod)

        # print(productback)
        productback.reverse()

        ans=[]
        for i, n in enumerate(productback):
            ans.append( productback[i] * productfwd[i])

        return ans

