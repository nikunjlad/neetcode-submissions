class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # we have a corner case here
        if len(s) != len(t):
            return False
        
        # we define a set of unique words
        unique = set(s)

        for ch in unique:
            if s.count(ch) != t.count(ch):
                return False

        return True
