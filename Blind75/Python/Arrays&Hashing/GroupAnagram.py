from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for word in strs:
            count = []
            for c in word:
                count[ord(c)-ord('a')]=+1
            res[tuple(count)].append(word)
        return list[res.values()]