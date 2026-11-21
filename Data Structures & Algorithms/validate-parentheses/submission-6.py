class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {}
        closeToOpen = {}
        closeToOpen[')'] = '('
        closeToOpen['}'] = '{'
        closeToOpen[']'] = '['
        stack = ["start"]
        for i in range(len(s)):
            if s[i] in closeToOpen:
                if stack[-1] != closeToOpen[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        if stack[-1] == "start":
            return True
        else:
            return False