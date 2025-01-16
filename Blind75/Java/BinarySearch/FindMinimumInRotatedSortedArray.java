package Blind75.BinarySearch;

import java.util.*;

public class FindMinimumInRotatedSortedArray {
    public int findMin(int[] nums) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i: nums)
        {
            heap.add(i);
        }
        int min = heap.poll();
        return min;
    }
}
