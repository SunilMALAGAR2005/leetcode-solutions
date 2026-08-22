class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nummap={}
        for i in range(len(nums)):
            if nums[i] in nummap:
                nummap[nums[i]]+=1
            else:
                nummap[nums[i]]=1
        for num in nummap:
            if nummap[num]>(len(nums)//2):
                return num
        
        