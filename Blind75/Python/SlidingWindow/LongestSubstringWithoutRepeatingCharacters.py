class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        length=0

        for r in range(len(s)-1):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            length=max(length,r-l+1)     
        return length

if __name__ == "__main__":
    sol =  Solution()
    s="abcabcbb"
    print(sol.lengthOfLongestSubstring(s))