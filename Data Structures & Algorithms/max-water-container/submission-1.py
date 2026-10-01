class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0 
        j = len(heights)-1 
        area= 0

        while  i< j:
            larea = (j-i) * min (heights[i] , heights[j])
            if larea > area:
                area = larea

            if heights[i] < heights[j]:
                i+=1
            elif heights[j] < heights[i]:
                j-=1
            elif heights[j] == heights[i]:
                i+=1
                j-=1
            
        
        return area


            


        