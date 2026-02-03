from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_elements = []
        set2 = set(nums2)
        for num1 in set(nums1):
            if num1 in set2:
                intersection_elements.append(num1)
        return intersection_elements

