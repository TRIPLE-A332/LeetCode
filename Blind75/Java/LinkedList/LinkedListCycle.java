package Blind75.LinkedList;
import java.util.*;

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ArrayList<ListNode> ne = new ArrayList<>();
        ListNode curr= head;
        while(curr != null)
        {
            if(ne.contains(curr))
            {
                return true;
            }
            ne.add(curr);
            curr = curr.next;
            
        }
        return false;
    }
}
