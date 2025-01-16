

public class productExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        
        int[] ans = new int[nums.length];
        int prod=1;
        ans[0] = 1;
        for(int i=1 ; i<nums.length ; i++)
        {
            ans[i] = prod*nums[i-1];
            prod*=nums[i-1];
        }
        int prod2=1;
        int post =1;
        for (int j=nums.length-1; j>0; j--)
        {
            post = nums[j]*prod2;
            ans[j-1] *= post;
            prod2*=nums[j];
        }

        return ans;
    }

}
