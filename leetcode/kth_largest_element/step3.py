import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self._k = k
       self.nums = nums
       heapq.heapify(self.nums)
       self._trim_nums_to_keep_size()

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self._trim_nums_to_keep_size(self)

        return self.kth_largest()

    def kth_largest(self):
        return self.nums[0]
    
    def _trim_nums_to_keep_size(self):
        while len(self.nums) > self._k:
            heapq.heappop(self.nums)
        