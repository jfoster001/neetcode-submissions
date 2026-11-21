class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #returns true if a value appears twice, false otherwise
        #nums length is positive, and its values can be all ints
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False