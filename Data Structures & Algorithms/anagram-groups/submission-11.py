class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # must : you have to iterate strs array, 
        # push sort and check if exist as value
        # No 
        # ans = [["hat"]]
        # Yes {ath : index 1}
        # push at ans[2].append[item]

        my_dict = {}
        ans =[]
        for item in strs:
            sorted_item= ''.join(sorted(item))
            if sorted_item in my_dict:
                ans[my_dict[sorted_item]].append(item)
            else :
                ans.append([item])
                my_dict[sorted_item] = len(ans) - 1
 
        return ans

