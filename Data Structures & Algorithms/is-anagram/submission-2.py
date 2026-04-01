class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if m != n:
            return False
        if sorted(s) == sorted(t):
            return True
        return False