class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 # Initialize variables
        d={} # use Dictionary to store last seen indics and key
        max_value =0 # max starting 0

        while r < len(s):
            if s[r] not in d: # s[r] Alphabet
                d[s[r]] = r #{ s[r] : index }
                max_value = max(max_value, r-l+1)
                r+= 1
            else:
                del d[s[l]] # we found same char so delte
                l+=1
        return max_value
        





