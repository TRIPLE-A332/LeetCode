import math
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l < r:
            currSum = numbers[l]+numbers[r]
            if currSum>target:
                r-=1
            if currSum<target:
                l+=1
            if currSum==target:
                return [l+1,r+1]
        return []
            

if __name__ == "__main__":
    numbers = [-1,0]
    target = -1
    sol = Solution()
    result = sol.twoSum(numbers, target)
    print(result)