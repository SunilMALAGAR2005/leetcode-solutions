class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen=set()
        dup=set()
         
        for num in nums:
            if num in seen:
                dup.add(num)
            else:
                seen.add(num)
        return list(dup)