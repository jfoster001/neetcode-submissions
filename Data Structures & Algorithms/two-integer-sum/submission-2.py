class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #goals: find the two indicies that total up  to target
        #constraints: length of array 2-1000, ranges from -10 mil to 10 mil

        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap and  hashmap[diff] !=i:
                return[i, hashmap[diff]]
        return[]