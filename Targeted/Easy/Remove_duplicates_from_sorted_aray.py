class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0
        k = 1

        for r in range(len(nums)):
            if nums[l]==nums[r]:
                continue
            else :
                temp = nums[r]
                nums[r] = nums[l+1]
                nums[l+1] = temp
                l += 1
                k += 1
        
        return k