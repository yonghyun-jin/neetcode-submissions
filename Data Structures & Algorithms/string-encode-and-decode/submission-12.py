class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            encoded_string += str(len(item)) + "#" + item  # Store length and content
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i  # Find the position of '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # Extract length
            word = s[j+1:j+1+length]  # Extract the actual string
            res.append(word)
            i = j + 1 + length  # Move to the next part

        return res
        