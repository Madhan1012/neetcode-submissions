class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                su = n + nums[l] + nums[r]

                if su < 0:
                    l += 1
                elif su > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return res