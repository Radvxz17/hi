class Solution:
    def isValid(self, s: str) -> bool:
        

        # can't start with a close
        # use hash to match an open matches a close


        stack = []

        closeToOpen = {")": "(", "]":"[", "}":"{"} 

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # match close and open
                    stack.pop()
                else:
                    return False # dont match 
            else:
                stack.append(c)
            
        if not stack:
            return True
        else:
            return False

        
       