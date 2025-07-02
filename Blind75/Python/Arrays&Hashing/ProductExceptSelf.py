from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prod=1
        prefix =1
        for i,num in enumerate(nums):
            



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print("Input:", nums)
    print("Output:", result)