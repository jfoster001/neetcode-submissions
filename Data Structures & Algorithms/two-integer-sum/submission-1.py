class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #goals: find the two indicies that total up  to target
        #constraints: length of array 2-1000, ranges from -10 mil to 10 mil

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        