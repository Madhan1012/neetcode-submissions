class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)

        return True if dict_s == dict_t else False