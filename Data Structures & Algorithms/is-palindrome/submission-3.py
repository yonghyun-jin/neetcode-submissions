class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  1 2 3 2 1 
        #  1 2 3 3 2 1
        #  if even = finsih there
        #  if odd, 5/2 = devider
        #  only run dvider for both
        # 6/2 = 3 times
        # 5/2 = 2 times
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        if len(cleaned) ==0:
            return True

        for index in range(0, len(cleaned)//2+1):
            if cleaned[index] != cleaned[len(cleaned)- index -1]:
                return False

        return True
        