class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        
        end = len(s)

        for i in range(end // 2):
            if s[i] != s[end - 1 - i]:
                return False

        return True