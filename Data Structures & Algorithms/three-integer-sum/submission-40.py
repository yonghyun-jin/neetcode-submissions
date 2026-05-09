class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res=[]

        for index, num in enumerate(arr):
            # first number = num
            i = index +1
            j = len(arr)-1
            if index > 0 and num == arr[index - 1]:
                continue

            

            while i < j:
                sum_value = num + arr[i]+ arr[j]
                if sum_value == 0:
                    res.append([num, arr[i], arr[j]])
                    
                    while i < j and arr[i] == arr[i + 1]:
                        i += 1
                    while i < j and arr[j] == arr[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
                elif sum_value > 0:
                    j -= 1
                else:
                    i += 1
        return res
