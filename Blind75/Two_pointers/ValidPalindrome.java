package Blind75.Two_pointers;
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
                int i=0 ,l = 0, r = s.length()-1;
        

        while(l<r)
        {
            char cl= s.charAt(l);
            char c1= Character.toLowerCase(cl); 
            char cr= s.charAt(r);
            char c2= Character.toLowerCase(cr); 
            
            if(l< r && !Character.isLetterOrDigit(c1))
            {
                l++;
                continue;
            }
            if(r>l && !Character.isLetterOrDigit(c2))
            {
                r--;continue;
            }
            
            if(c1 != c2)
            {
                return false;
            }
            l++;
            r--;
        }
        return true;


        
        
        
        /*
        StringBuilder sc = new StringBuilder();
        for (int i=0; i<s.length() ; i++)
        {
            char c = s.charAt(i);
            if(c>='0' && c<='9')
            {
                sc.append(c);
            }
            if(c>='a' && c<='z')
            {
                sc.append(c);
            }
            if(c>='A' && c<='Z')
            {
                char ch = Character.toLowerCase(c);
                sc.append(ch);
            }
        }
        String sc2 = sc.toString();
        String snew = sc.reverse().toString();
        if (snew.equals(sc2)){return true;}
        else {return false;}
        */
    }

    public static void main(String[] args) {
        ValidPalindrome vp = new ValidPalindrome();
        String ppp = "A man, a plan, a canal: Panama";
        System.out.println(vp.isPalindrome(ppp));
    }
}
