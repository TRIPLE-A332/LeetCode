#iteration

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if max(p.val , q.val) < curr.val:
                curr = curr.left
            elif min(p.val , q.val) > curr.val:
                curr = curr.right
            else:
                return curr
         

#recursion
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if max(p.val , q.val) < root.val:
            return self.lowestCommonAncestor(root.left , p , q)
        elif min(p.val , q.val) > root.val:
            return self.lowestCommonAncestor(root.right , p , q)
        else:
            return root
