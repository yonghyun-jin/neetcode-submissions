class Solution:

    def encode(self, strs: List[str]) -> str:
        # Pattern = D8)
        # D8)neetD8)code
        result = ""
        for item in strs:
            result = result+item+")C8!"
        print(result)

        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        cache = ""
        while i < len(s):
            if s[i:i+4] == ")C8!" and i+3 < len(s):
                # [0,1,2,3,4,5,6]
                #  ) C 8 )
                i = i + 4
                result.append(cache)
                cache = ""
            else:
                cache = cache + s[i]
                i = i+1
        
        return result





