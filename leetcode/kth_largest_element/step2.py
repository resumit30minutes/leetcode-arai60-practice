import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self._first_k_min_heap = nums
        heapq.heapify(self._first_k_min_heap)

        while len(self._first_k_min_heap) > self.k:
            heapq.heappop(self._first_k_min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._first_k_min_heap, val)

        if len(self._first_k_min_heap) > self.k:
            heapq.heappop(self._first_k_min_heap)

        return self.kth_largest()

    def kth_largest(self):
        return self._first_k_min_heap[0]
