class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT={}
        for c in t:
            countT[c]= 1 + countT.get(c,0)
    
        l=0
        mini = {}
        sub=""
        for r in range(len(s)):
            sub+=s[r]
            if s[r] in countT.keys():
                countT[s[r]]-=1
            if max(countT.values())==0:
                mini[sub] = len(sub)
                sub=""
                l+=1
                r=l
                for c in t:
                    countT[c]= 1 + countT.get(c,0)
        if not mini:
            return ""
        return min(mini, key=mini.get)
    
if __name__ == "__main__":
    sol = Solution()
    s ="ADOBECODEBANC"
    t ="ABC"
    print(sol.minWindow(s,t))