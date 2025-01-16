from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            t = target - x
            for j,y in enumerate(nums):
                if j!=i and y==t:
                    res = [i,j]
                    return res