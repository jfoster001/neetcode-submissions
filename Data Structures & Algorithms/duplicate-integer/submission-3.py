class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #returns true if a value appears twice, false otherwise
        #nums length is positive, and its values can be all ints
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False