class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        d={}
        max_value =0

        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
                max_value = max(max_value, r-l+1)
                r+= 1
            else:
                del d[s[l]]
                l+=1
        return max_value
        





