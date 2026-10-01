class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        valleys = []
        i = 0

        while i < n - 1:
            if height[i] > height[i + 1]:
                start = i
                j = i + 1


                max_h = height[j]
                max_pos = j

                while j < n:
                    if height[j] >= height[start]:
                
                        end = j
                        valleys.append((start, end))
                        i = end
                        break

                    if height[j] > max_h:
                        max_h = height[j]
                        max_pos = j
                    j += 1
                else:
                    end = max_pos
                    valleys.append((start, end))
                    i = end
            else:
                i += 1
        
        total_water = 0
        for start, end in valleys:
            bound_height = min(height[start], height[end])
            for k in range(start + 1, end):
                trapped = bound_height - height[k]
                if trapped > 0:
                    total_water += trapped

        return total_water

             
            
        