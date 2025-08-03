
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def printList(head):
        vals = []
        while head:
            vals.append(str(head.val))
            head = head.next
        print("->".join(vals))

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr , prev = head , None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

if __name__ == "__main__":
    # Create linked list 1->2->3->4->5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print("Original list:")
    ListNode.printList(n1)

    sol = Solution()
    reversed_head = sol.reverseList(n1)

    print("Reversed list:")
    ListNode.printList(reversed_head)
    ln.printList(reversed_head)