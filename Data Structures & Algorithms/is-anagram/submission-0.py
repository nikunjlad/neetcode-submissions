class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # we have a corner case here
        if len(s) != len(t):
            return False
        
        # we define a hashmap for each string
        s_dict = Counter()
        t_dict = Counter()

        # next we loop over each string length to ensure we register the count
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True
        else:	
            return False
