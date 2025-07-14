class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        maxf=0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1

            maxf = max(maxf,r-l+1)
        return maxf
    
if __name__ == "__main__":
    sol = Solution()
    s ="ABBA"
    k =2
    print(sol.characterReplacement(s,k))