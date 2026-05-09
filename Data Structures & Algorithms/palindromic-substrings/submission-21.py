class Solution:
    def countSubstrings(self, s: str) -> int:
        # 0: [prev] + [new calculation]  = 
        # 1: [0] + [new calculaton]
        # new calculation 
        # edge cases
        # len = 0
        # len = 1 

        if len(s) < 2 : return len(s)

        result = 0

        for i in range(len(s)):
            for j in range(i + 1):
                print(s[j:i + 1])
                if self.helper(s[j:i + 1]): result += 1

        return result

    def helper(self, arr):
        if arr == arr[::-1]:
            return True
        return False


    #     if len(s) == 0:
    #         return 0
        
    #     result = 0
    #     for i, n in enumerate(s):
    #         arr = s[0:i+1]
          
    #         save = []
    #         for item in arr[::-1]:
    #             print(save)
    #             save.append(item)

    #             # palindrom
    #             if self.helper(save):
    #                 result=+1
            
    #     return result



    # def helper(self, arr):
    #     # if len(arr) < 2: return True
    #     # return arr[0] == arr[-2] and self.helper(arr[1:-1])
    #     if arr == arr[::-1]:
    #         return True
    #     return False
