class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxLen = 0
        length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    maxLen = max(length, maxLen)
        
        return maxLen
            

if __name__ == "__main__":
    sol =  Solution()
    s ="(()"
    print(sol.longestValidParentheses(s))