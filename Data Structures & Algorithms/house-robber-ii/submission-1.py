class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def rob_house(houses):
            if len(houses) == 1:
                return houses[0]

            n = len(houses)
            dp = [0] * n

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + houses[i]
                )
            
            return dp[n-1]
        
        return max(
            rob_house(nums[:-1]),
            rob_house(nums[1:])
        )