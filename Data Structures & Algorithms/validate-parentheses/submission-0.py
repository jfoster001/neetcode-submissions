class Solution:
    def isValid(self, s: str) -> bool:
      #true if every bracket is closed correctly
      #push bracket onto stack. if closing bracket, check if corresponding opening bracket
      stack = []
      closeOpen= {')':'(', ']':'[', '}':'{'}
      for c in s:
        if c in closeOpen:
            if stack and stack[-1] == closeOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
      return False if stack else True
