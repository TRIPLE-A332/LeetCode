import java.util.*;

public class TopKfrequentElements {

    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hmap = new HashMap<>();
        
        for (int i : nums)
        {
            hmap.put(i,hmap.getOrDefault(i,0)+1);
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>();

        for (Map.Entry<Integer,Integer> entry : hmap.entrySet())
        {
            int[] n = {entry.getValue(), entry.getKey()};
            heap.add(n);
            if(heap.size()>k)
            {
                heap.poll();
            }
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = heap.poll()[1];
        }

        return res;
    }
    
}
