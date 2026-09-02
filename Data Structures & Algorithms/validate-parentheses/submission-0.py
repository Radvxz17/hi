class Solution:
    def isValid(self, s: str) -> bool:
        

        # can't start with a close
        # use hash to match an open matches a close

        stack  = []


        hash = {")":"(", "]":"[", "}":"{"}


        for c in s:
            if c in hash:
                if stack and stack[-1] == hash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False


       