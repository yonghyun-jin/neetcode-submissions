from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for index in range(n):
            # index 기준 중복 스킵
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            l = index + 1
            r = n - 1

            # 남은 원소가 2개 미만이면 종료
            if r - index < 2:
                break

            while l < r:
                sum_num = nums[index] + nums[l] + nums[r]

                if sum_num > 0:
                    r -= 1
                elif sum_num < 0:
                    l += 1
                else:
                    res.append([nums[index], nums[l], nums[r]])

                    # 다음 후보로 이동
                    l += 1
                    r -= 1
                    # 틀리는 부분
                    # l 중복 스킵
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # r 중복 스킵
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
