class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)):
            return False
        hash_map={}
        for ch in range(len(s)):
            if t[ch] not in hash_map:
                hash_map[t[ch]]=s[ch]
            elif hash_map[t[ch]]!=s[ch]:
                return False
        return True
                