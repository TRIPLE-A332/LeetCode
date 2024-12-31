
import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()){ return false;}
        HashMap<Character,Integer> mapS = new HashMap<>();
        HashMap<Character,Integer> mapT = new HashMap<>();

    for ( int n=0 ; n<s.length() ; n++)
    {
        mapS.put(s.charAt(n), mapS.getOrDefault(s.charAt(n),0)+1);
        mapT.put(s.charAt(n), mapT.getOrDefault(s.charAt(n),0)+1);
    }
        return mapS.equals(mapT);
    }
}

class Anagram{
    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "rat";
        String t = "cat";
        System.out.println(sol.isAnagram(s, t));

    }
}