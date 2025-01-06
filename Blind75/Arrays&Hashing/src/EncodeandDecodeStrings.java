import java.util.*;

public class EncodeandDecodeStrings {
    public String encode(List<String> strs) {
        
        StringBuilder ab = new StringBuilder();
        for(String s : strs)
        {
            int length = s.length();
            ab.append(length).append('$').append(s);

        }
        return ab.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> arl = new ArrayList<>();
        int i =0;
        while (i<str.length())
        {
            int j = i;
            while(str.charAt(j) != '$')
            {
                j++;
            }
            int len = Integer.parseInt(str.substring(i,j));
            i = j+1;
            j = j+ len;
            arl.add(str.substring(i,j));
            i = j;
        }
        return arl;
    }

    public static void main(String[] args) {
        EncodeandDecodeStrings e = new EncodeandDecodeStrings();
        List<String> asd = new ArrayList<>(Arrays.asList("neet","code","love","you"));
        System.out.println(e.encode(asd));
        
        
    }

}
