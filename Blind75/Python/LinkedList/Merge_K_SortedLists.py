class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        incNum = []

        for l in lists:
            while l:
                incNum.append(l.val)
                l = l.next
        
        incNum.sort()

        dummy = ListNode(0 , None)
        tail = dummy

        for node in incNum:
            tail.next = ListNode(node)
            tail = tail.next
        
        return dummy.next
