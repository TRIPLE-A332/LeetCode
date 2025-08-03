class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        
        return False
    

#2nd ans
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head , head

        while slow or fast:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                return True       
        return False