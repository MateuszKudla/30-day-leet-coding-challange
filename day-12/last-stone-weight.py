from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, -abs(stone1 - stone2))

        if len(heap) == 1:
            return -heap[0]

        return 0

if __name__ == "__main__":
    solution = Solution()
    result = solution.lastStoneWeight([2,7,4,1,8,1])
    print (result)