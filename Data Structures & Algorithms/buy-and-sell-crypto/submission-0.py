class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        minP = float("inf")
        
        for p in prices:
            if p < minP:
                minP = p
            elif p - minP > maxP:
                maxP = p - minP
        return maxP