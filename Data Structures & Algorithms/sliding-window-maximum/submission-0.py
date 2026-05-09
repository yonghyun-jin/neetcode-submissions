class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of this window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove smaller values from the back
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

            # Add current index
            deq.append(i)

            # If window is full, add the current max to result
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result