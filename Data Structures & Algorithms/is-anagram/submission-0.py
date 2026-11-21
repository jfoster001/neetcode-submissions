class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return true if strings s and t are the same, false       otherwise
        #strings are not empty and are all lowercase
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)