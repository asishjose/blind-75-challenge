class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = nums[0]
        curmax, curmin = 1,1
        for n in nums:
            temp = curmax*n
            curmax = max(temp, curmin*n, n)
            curmin = min(temp, curmin*n, n)
            result = max(curmax, result)
        return result