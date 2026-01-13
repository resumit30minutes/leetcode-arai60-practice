from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [((nums1[0] + nums2[0]), 0, 0)]
        added = set()
        
        def need_to_add(x, y):
            if x >= len(nums1) or y >= len(nums2):
                return False
            if x == 0 or y == 0:
                return True
            return (x - 1, y) in added and (x, y - 1) in added
        
        def add_candidates_if_necessary(x, y):
            if need_to_add(x, y):
                heapq.heappush(((nums1[x] + nums2[y]), x, y))
        
        pairs = []
        while k < len(pairs) and candidates:
            _, i, j = heapq.heappop(candidates)
            pairs.append([nums1[i], nums2[j]])
            added.add((i, j))
            add_candidates_if_necessary(i + 1, j)
            add_candidates_if_necessary(i, j + 1)

        return pairs
        
