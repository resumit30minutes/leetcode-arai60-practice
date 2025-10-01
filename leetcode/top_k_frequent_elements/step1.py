import collections, heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_fequency  = collections.defaultdict(int)
        for num in nums:
            num_to_fequency[num] += 1

        top_k_frequent = []
        for num, frequency in num_to_fequency.items():
            heapq.heappush(top_k_frequent, (frequency, num))
            if len(top_k_frequent) > k:
                heapq.heappop(top_k_frequent)
        
        return [num for frequency, num in top_k_frequent ]
