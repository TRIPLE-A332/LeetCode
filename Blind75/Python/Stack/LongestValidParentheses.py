class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        maxLen = 0

        for i in range(len(s)):
            

if __name__ == "__main__":
    sol =  Solution()
    s ="(()"
    print(sol.longestValidParentheses(s))