from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l < r:
            mid =  (l + (r - l)) // 2
            if nums[mid] >= target and nums[l] <= target:
                if target == nums[mid]:
                    return mid
                if target == nums[l]:
                    return l
                if target == nums[r]:
                    return r
                else:
                    r = mid - 1

            else: 
                l = mid+1 
                mid =  (l + (r - l)) // 2
                if target == nums[mid]:
                    return mid
                if target == nums[l]:
                    return l
                if target == nums[r]:
                    return r
        
        return -1
    

if __name__ == "__main__" :
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums,target))