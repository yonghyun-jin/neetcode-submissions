# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # Search algorithm with O(log n) we should use binary search
#         # Given : Rotated Sorted array, Target number
#         # Edge case: there could be no matchin number

#         # l m r
#         # 3 5 2 
#         # 1. find sorted side
#         # 2. find if sorted side contain the target
#         #     sorted side contain the target -> update l and r
            
#         # 3. Sorted side does not contain the target
#         #     -> update l and r
#         # repeat until l < r

#         # at the end returm nums[m]
#         # l,r = 0, len(nums)-1
#         # target = -1
            
#         while l < r: 
#             m = (l+r)//2
#             if nums[m] == target:
#                 return m

#             if nums[m] > nums[l]:
#                 # left side is sorted 1 2 3 4 5 6 7
#                 if nums[l] <= target and nums[m] <= target:
#                     r = m
#                 else:
#                     l = m+1
#             else:
#             # elif nums[m] < nums[r]
#                 # right side is sorted 
#                 # [3,5,0,1,2]
#                    l.  m.    r
#                 if nums[m] <= target and nums[r] <=target:
#                     l = m
#                 else:
#                     r = m-1

#             if nums[m] == target:
#                 return m
#         return -1
        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Search algorithm with O(log n) complexity — use binary search
        # Given: Rotated sorted array, and a target number
        # Edge case: There may be no matching number

        # Binary search logic:
        # 1. Find which side is sorted
        # 2. Check if the sorted side contains the target
        #    - If it does, update l and r to narrow to that side
        #    - If not, update l and r to exclude that side
        # Repeat until l <= r

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Left side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right side is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
