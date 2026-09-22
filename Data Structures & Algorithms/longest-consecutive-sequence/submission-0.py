class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if n - 1 not in numset:
                currnum = n
                curr = 1
                while currnum + 1 in numset:
                    currnum += 1
                    curr += 1
                longest = max(longest, curr)
        return longest