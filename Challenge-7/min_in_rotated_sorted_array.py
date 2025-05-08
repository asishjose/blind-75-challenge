class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        if nums[left]<nums[right]:
            return nums[0]
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid]>nums[0]:
                    right = mid
                else:
                    left = mid
