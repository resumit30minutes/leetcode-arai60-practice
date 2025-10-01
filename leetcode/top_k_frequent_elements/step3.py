import collections, heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = collections.defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1

        sorted_frequency_num_pair_list = []
        for num, frequency in num_to_frequency.items():
            heapq.heappush(sorted_frequency_num_pair_list, (frequency, num))

            if len(sorted_frequency_num_pair_list) > k:
                heapq.heappop(sorted_frequency_num_pair_list)

        return [ num for frequency, num in sorted_frequency_num_pair_list ]