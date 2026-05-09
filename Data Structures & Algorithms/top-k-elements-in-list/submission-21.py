class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Objective: return the k most frequent element withint the array
        # Given : nums of array, value k
        # O(n)
        # no nulls in nums
        # k is bigger than 0

        # key = value of number
        # value = freq

        # d = {}
        # output = []

        # for loop to create the map

        # another loop that go through the map

        # and making the output array

        # O(2N)

        d ={}
        output = []

        for item in nums:
            if item in d:
                d[item] = d[item] +1
            else:
                d[item] = 1
        
        arr = []
        for num, cnt in d.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res



    #     for key, value in my_dict.items():
    # print(f"Key: {key}, Value: {value}")


        return output

