class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        to_return = []
        for num in nums2:
            if num in seen:
                to_return.append(num)
                seen.remove(num)
        return to_return