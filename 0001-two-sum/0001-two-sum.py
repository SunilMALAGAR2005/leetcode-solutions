class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nmap={}
        for i in range(n):
            comp=target-nums[i]
            if comp in nmap:
                return [nmap[comp],i]
            else:
                nmap[nums[i]]=i
        return []
        

        