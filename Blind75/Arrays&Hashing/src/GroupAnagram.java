
import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String , List<String>> hmap = new HashMap<>();
        
        for (String s : strs)
        {
            int[] count = new int[26];
            for ( char c : s.toCharArray())
            {
                count[c-'a']++;
            }
            String key = Arrays.toString(count);
            hmap.putIfAbsent(key, new ArrayList<String>());
            hmap.get(key).add(s);
        }
        return new ArrayList<>(hmap.values());
        
    }
}

public class GroupAnagram{
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        
        System.out.println(sol.groupAnagrams(strs));

    }
}