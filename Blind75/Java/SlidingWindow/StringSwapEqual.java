public class StringSwapEqual {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.equals(s2)){return true;}
        int l=0;
        int r=s2.length()-1;
        StringBuilder sb2 = new StringBuilder(s2);
        while(l<=r)
        {   
            char temp = s2.charAt(r);
            sb2.setCharAt(r,s2.charAt(l));
            sb2.setCharAt(l,temp);
            l++;
            r--;
        }
        return s1.equals(sb2.toString());
    }
    public static void main(String[] args) {
        StringSwapEqual sc = new StringSwapEqual();
        String s1 = "bank";
        String s2 ="knab";
        System.out.println(sc.areAlmostEqual(s1, s2));
    }
}
