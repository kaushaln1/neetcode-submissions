class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0 
        r= len(nums)-1
        mid = (l+r)//2
        if nums[l] <nums[r]:
            return nums[l]
        while (l<r):
            if (nums[r] >nums[mid] ):
                r= mid
                mid = (l+r)//2

            else: 
                l= mid+1
                mid = (l+r)//2
        
        return nums[l]