import heapq
import itertools

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = [(nums1[0] + nums2[0], (0, 0))]
        seen = set([(0, 0)])
        pairs = []
        while len(pairs) < k:
            total, (i, j) = heapq.heappop(candidates)
            pairs.append((nums1[i], nums2[j]))
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(candidates, (nums1[i + 1]+nums2[j], (i + 1, j)))
                seen.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(candidates, (nums1[i] + nums2[j + 1], (i, j + 1)))
                seen.add((i, j + 1))
        return pairs

    def solution1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return map(list, sorted(itertools.product(nums1, nums2), key=sum)[:k])
    
    def solution2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]