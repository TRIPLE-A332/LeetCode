package Blind75.BinarySearch;

public class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {
        int l =0,r=nums.length-1;
        int mid=(l+r)/2;
        if(nums.length == 0)
        {return -1;}
        if(nums.length == 1 && target==nums[0])
        {return 0;}
        if(nums.length == 1 && target!=nums[0])
        {return -1;}
        if(nums[l]==target){return l;}
        if(target==nums[mid]){return mid;}
        if(nums[r]==target){return r;}
        if(nums[l]>=nums[r])
        {   
            for(int i =0; i<nums.length; i++)
            {
                int d = nums[i] - nums[i+1];
                if(d>0)
                {
                    mid = i;
                    break;
                }
            }
        }
        while (l<=mid || r>=mid) 
        {       
            if(target<=nums[mid]&&target>=nums[l])
            {
                if(nums[l]==target){return l;}
                if(target==nums[mid]){return mid;}
                if((mid-l)==1){return-1;}
                r=mid-1;
                mid = (l+r)/2;
                continue;
            }
            if (target>=nums[mid+1]&&target<=nums[r])
            {
                if(target==nums[mid]){return mid;}
                if(nums[r]==target){return r;}
                if((r-(mid+1))==1){return-1;}
                l=mid+1;
                mid=(l+r)/2;
                continue;
            }
            return -1;
        }
        return -1;
    }
    public static void main(String[] args) {
        SearchInRotatedSortedArray s = new SearchInRotatedSortedArray();
        int[] nums = {5,1,3};
        System.out.println(s.search(nums, 0));
    }
}
