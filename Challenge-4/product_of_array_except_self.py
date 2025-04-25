class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(n - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
        return answer

