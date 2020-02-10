import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    heap = []
    for value in stones:
        heapq.heappush(heap, -value)

    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -abs(a - b))

    return -heap[0] if len(heap) == 1 else 0


print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
