package Blind75.SlidingWindow;
import java.util.*;

public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
     
        
        StringBuilder sc = new StringBuilder();
        int max=0;
        if(s.length()==0){return 0;}
        if(s.length()==1){return 1;}
        int l=0,r=1;
        sc.append(s.charAt(l));
        while(r<s.length())
        {
            if(s.charAt(l)!=s.charAt(r))
            {   
                for(int i=0; i<sc.length() ;i++)
                {
                    
                    if(s.charAt(r)== sc.charAt(i) )
                    {   
                        max = Math.max(sc.length(),max);
                        sc.delete(0, i+1);
                        l = l + i +1;
                        break;                                            
                    }              
                }
                
                
                sc.append(s.charAt(r));
                max = Math.max(sc.length(),max);
                r++;
                continue;                
                
            }
            if(s.charAt(l)==s.charAt(r))
            {
                max = Math.max(sc.length(),max);
                sc.deleteCharAt(0);
                sc.append(s.charAt(r));
                l++;
                r++;
                
            }
        }
        
        return max;

    }
    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters l = new LongestSubstringWithoutRepeatingCharacters();
        String s = "au";
        System.out.println(l.lengthOfLongestSubstring(s));
    }
}
