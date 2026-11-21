class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_result = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_result = max(max_result, cur_sum)
        return max_result