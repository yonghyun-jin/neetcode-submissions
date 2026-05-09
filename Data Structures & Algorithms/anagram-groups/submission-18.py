class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for item in strs:
            key = ''.join(sorted(item))
            if key not in seen:
                seen[key] = []
            seen[key].append(item)

        result = []
        for value in seen.values():
            result.append(value)

        return result





            


                


        # At the end
        # Loop through the dictionary
        # key should be the sorted value
        # Value should be array


