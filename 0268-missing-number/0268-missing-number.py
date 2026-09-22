class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            res=res^nums[i]^i
        return res^n
        