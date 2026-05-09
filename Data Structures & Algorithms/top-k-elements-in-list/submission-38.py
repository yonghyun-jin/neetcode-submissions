from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []  # (count, num)

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)  # 가장 작은 빈도 제거

        # heap에는 k개가 남아있고, (count, num) 형태
        return [num for count, num in heap]