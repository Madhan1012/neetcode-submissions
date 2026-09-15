class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mappings = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in mappings.values():
                stk.append(c)
            elif c in mappings.keys():
                if not stk:
                    return False
                top = stk.pop();
                exp = mappings[c]
                if top != exp:
                    return False
        if not stk:
            return True
        return False
