class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Move left pointer until we find a valid alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1

            # Move right pointer until we find a valid alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare current left and right (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # Move inward after a successful match
            l += 1
            r -= 1

        return True
