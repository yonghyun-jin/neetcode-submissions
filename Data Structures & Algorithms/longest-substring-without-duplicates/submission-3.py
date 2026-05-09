class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0  # Start pointers at 0
        char_map = {}  # Store characters and their last seen indices
        max_value = 0  # Track the maximum length found

        while r < len(s):  # Use `and`, not `or`
            if s[r] not in char_map:
                char_map[s[r]] = r  # Store character with index
                max_value = max(max_value, r - l + 1)  # Update max length
                r += 1  # Expand window
            else:
                del char_map[s[l]]  # Remove leftmost character from map
                l += 1  # Move left pointer

        return max_value