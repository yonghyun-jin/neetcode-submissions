class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res = res + str(len(item)) + "#" + item
        return res

    def decode(self, s: str) -> List[str]:
        res,i = [],0


        while i < len(s): 
            j=i
            while s[j] != "#": # 1234# 1234 of char word
                j+=1
            length = int(s[i:j]) # find the 1234
            string = s[j+1:j+1+length]
            res.append(string)
            i = j+1+length
        return res





        