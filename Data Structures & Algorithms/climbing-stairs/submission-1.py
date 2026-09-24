class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        v1, v2 = 1, 1
        for i in range(1, n):
            v1, v2 = v2, v1 + v2
        return v2
            