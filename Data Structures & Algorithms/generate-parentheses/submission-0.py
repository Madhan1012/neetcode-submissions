class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = [] 

        def backtrack(openB, closeB):
            if openB == closeB == n:
                res.append("".join(path[:]))
                return
            if openB < n:
                path.append("(")
                backtrack(openB + 1, closeB)
                path.pop()
            if closeB < openB:
                path.append(")")
                backtrack(openB, closeB + 1)
                path.pop()
        
        backtrack(0, 0)
        return res