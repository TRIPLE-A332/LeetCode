from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix =1
        for i in range(len(nums)-1):
            res[i] = prefix
            prefix*=nums[i]
            
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print("Input:", nums)
    print("Output:", result)