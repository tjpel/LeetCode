class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for char in s:
            if not s.count(char) == t.count(char):
                return False

        if not len(s) == len(t):
            return False
        
        return True