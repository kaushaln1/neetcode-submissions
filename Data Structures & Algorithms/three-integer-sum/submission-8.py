class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        ans = []
        for i,num in enumerate(nums):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            target = -(num)
            print(target)
            l =i+1 
            r = len(nums)-1
            localarray = []
            while (l<r):
                print(" lkeft , roght ", nums[l], nums[r])
                if nums[l] + nums[r] == target:
                    localarray.append(nums[l]) 
                    localarray.append(nums[r])
                    localarray.append( num)
                    ans.append(localarray)
                    localarray = []
                    l+=1
                    r-=1
                    while (l<r and  nums[l] == nums[l-1]):
                        l+=1
                    while (r>l and nums[r] == nums[r+1]):
                        r-=1
                
                elif nums[l] + nums[r] > target :
                    r-=1
                elif nums[l] + nums[r] < target :
                    l+=1
                   
            

        return ans
        
























        # #case 1 
        # if 0 in map:
        #     for num in nums:
        #         if num== 0:
        #             break
        #         if -num in map:
        #             ans.append([num, 0 , -num])
        
        #case2
        # for i, num in enumerate(nums): 
        #     target = -num
        #     copymap = map
        #     for j , n in enumerate(nums):
        #         if i!=j :
        #             diff = target - n
        #             if diff in copymap and copymap[diff]>=0 and copymap[n]>=0:
        #                 copymap[diff]-=1
        #                 copymap[n]-=1
        #                 ans.append([num ,n , diff])
        # return ans




        