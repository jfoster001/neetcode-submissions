class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = []
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums:
                for j in range(len(nums)):
                    if nums[j] == needed and j != i:
                        myList.append(j)
                        myList.append(i)
                        myList.sort()
                        return myList
        return myList