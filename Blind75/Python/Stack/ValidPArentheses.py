class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        hmap = {')':'(' , ']':'[', '}':'{'}

        for c in s:
            if c in hmap:
                if stack and stack[-1] == hmap[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)

        return True if not stack else False