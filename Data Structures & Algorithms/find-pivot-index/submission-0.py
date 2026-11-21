class Solution:
    def get_sum_before(self, i, nums):
        if i == 0:
            return 0
        sum = 0
        for i in range(0, i):
            sum += nums[i]
            i -= 1
        return sum
    
    def get_sum_after(self, i, nums):
        if i == len(nums)-1:
            return 0
        sum = 0
        for i in range(i+1, len(nums)):
            sum += nums[i]
        return sum

    def pivotIndex(self, nums: List[int]) -> int:
        #return index that has a sum of all less numbers equal to all right numbers. else return -1
        
        for i in range(len(nums)):
            if self.get_sum_before(i, nums) == self.get_sum_after(i, nums):
                return i
        return -1