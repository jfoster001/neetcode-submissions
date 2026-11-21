class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return True if string is the same as reversed string
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        for i in range(len(s) // 2):
            if s[i].isalpha() or s[i].isdigit():
                if s[i] != s[len(s) - 1 - i]:
                    return False
        return True