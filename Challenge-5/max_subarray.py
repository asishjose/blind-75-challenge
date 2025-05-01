class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum += n
            if max_sum<curr_sum:
                max_sum = curr_sum
        return max_sum