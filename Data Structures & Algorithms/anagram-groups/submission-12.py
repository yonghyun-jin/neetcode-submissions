class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for item in strs:
            sort = "".join(sorted(item))
            print(sort)
            if sort in d:
                d[sort].append(item) 
            else:
                d[sort] = [item]
        res =[]
        for item in d:
            res.append(d[item])
        return res
        