from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            
            else:
                if not stack:
                    return False
                    
                cur = stack.pop()
                
                if (cur == "(" and i != ")") or (cur == "{" and i != "}") or (cur == "[" and i != "]"):
                    return False
        if stack:
            return False
        return True