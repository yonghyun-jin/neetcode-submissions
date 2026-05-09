class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)

        print(a)
        print(b)

        if a == b :
            return True
        return False