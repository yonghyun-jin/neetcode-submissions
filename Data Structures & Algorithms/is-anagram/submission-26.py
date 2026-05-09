class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # What is anagram?
        # contain same words
        # Sort the array first. and go over one by one from beginning, 
        # if there's difference we skip

        # Length comparison
        if len(s) != len(t):
            return False

        # sort
        sort_s = sorted(s) # sort return array
        sort_t = sorted(t)


        for i in range(0,len(s)):
            if sort_s[i] != sort_t[i]:
                return False

        return True
            



