class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        d={} # { s[r] : index}
        max_value=0
        # calculate the max

        # When to move right and left pointer
        # Move the right pointer when d doesn't contain s[r]
        # Move left pointer when there is duplicate
            # we need to delete from the d
            # 
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
                max_value = max(max_value, r-l+1)
                r = r+1

            else:
                del d[s[l]]
                l = l+1


        return max_value
        





