class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit= []
        min = prices[0]
        for p in prices:
            if p <min:
                min = p
            profit.append(p-min)
        max = 0
        for prof in profit:
            if prof > max:
                max= prof
        return max

        