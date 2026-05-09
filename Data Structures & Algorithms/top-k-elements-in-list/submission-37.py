class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Find nums counting by number
        count = {}
        reverse = {}
        output = []
        for item in nums:
            if item in count:
                count[item] = count[item] +1
            else:
                count[item] = 1
        
        for item,number in count.items():
            if number in reverse:
                # Mistake made here
                # reverse[number] = (reverse[number]).append(item)
                reverse[number].append(item)
            else:
                reverse[number] = [item]
        # Reverse = {count, item}


        print(reverse)
        for i in range(len(nums), -1, -1):

            if reverse.get(i):
                for index in range(0,len(reverse.get(i)) ):
                    if len(output) < k:
                        output.append(reverse[i][index])
                    else:
                        return output
                
        return output

