
import java.util.HashSet;

public class longestConsecutive {

    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hset = new HashSet<>();
        for(int n: nums)
        {
            hset.add(n);
        }

        int count = 0 ;
        for(int n: hset)
        {
            
            if(!hset.contains(n-1))
            {   
                int fro = 0;
                while(hset.contains(n+fro))
                {fro++;}
                count = Math.max(count,fro);
            }
            
        }
        return count;
    }
}

