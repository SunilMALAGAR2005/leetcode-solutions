class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s=sum(ord(ch) for ch in s)
        sum_t=sum(ord(ch) for ch in t)
        return chr(sum_t-sum_s)

        