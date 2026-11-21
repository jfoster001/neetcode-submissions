class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    my_set.add(i)
                    break
        return list(my_set)