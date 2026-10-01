class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #concatenate the array into a single array. then binary search

        array= [element for row in matrix for element in row]
        # for nums in matrix :
        #     array.extend(nums) 

        print (array)     
        return self.binarySearch(array,target)




    def binarySearch(self , array: List[int], target:int) -> bool:

        start =0 
        end= len(array)-1

        while (start <= end):
            mid = (start+end) //2 
            if target == array[mid]:
                return True
            if target < array[mid]:
                end = mid-1 
            else:
                start = mid+1
        
        return False


        