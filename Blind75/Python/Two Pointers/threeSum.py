from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if num>0:
                return res
            
            if i>0 and num == nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum= num + nums[l] + nums[r] 
                if threeSum > 0:
                    r-=1
                if threeSum < 0:
                    l+=1
                if threeSum==0:
                    res.append([num , nums[l] , nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res