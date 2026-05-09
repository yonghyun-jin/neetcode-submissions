class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return k most frequent number
        # 1 : 1, 2: 2
        # 1 : 1,  2 : 2, 3
        # 1 2 3
        # 2 1 
        # 1 2 2 
        # 1 2:2 
        # How can we save order?
        # or is there any other way we can sort by order?
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] = my_dict[num]+1
            else:
                my_dict[num] = 1
        arr=[]

        for key, value in my_dict.items():
            arr.append([value,key])

        arr.sort() # count, 
        res = []
        for i in range(0,k):
            res.append(arr.pop()[1])
        
        return res

