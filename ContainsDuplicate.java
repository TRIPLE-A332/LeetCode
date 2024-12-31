
import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hset = new HashSet<Integer>();
        
        for (int i : hset)
        {
            hset.add(i);
        }
        if (hset.size()<nums.length-1){return true;}
        else 
        return false;
    }
}
class ContainsDuplicate{
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1,2,3,4};
        
        System.out.println(sol.containsDuplicate(nums));

    }
}