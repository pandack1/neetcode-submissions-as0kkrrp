class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(","}":"{","]":"["}
        stack = []
        f = 0
        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in map.values():
                    stack.append(char)
                    f = 1
                else:
                    if stack and map[char] != stack[-1]:
                        return False
                    elif stack and map[char] == stack[-1]:
                        stack.pop()
            
            if len(stack) == 0 and f==1:
                return True
            else:
                return False
                



        