from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        w_e = "!"
        l_e = "@"
        res=""
        for s in strs:
            for c in s:
                res += str(ord(c))
                res += l_e
            res += w_e            
        return res

    def decode(self, s: str) -> List[str]:
        dec =[]
        analyse = ''
        final=''
        for c in s:
            if c =='!':
                dec.append(final)
                final=''
            elif c == '@':
                final += chr(int(analyse))
                analyse = ''
            else:
                analyse +=c
        return dec





if __name__ == "__main__":
    sol = Solution()
    strs = ["hello", "world", "leetcode"]
    encoded = sol.encode(strs)
    print("Encoded:", encoded)
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)