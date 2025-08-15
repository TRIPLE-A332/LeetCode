#iterative

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n+=1

            if n == k:
                return curr.val
            curr = curr.right
        

#recursive

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []
        
        def dfs(node):
            if not root:
                return None
            
            nodes.append(root.val)

            dfs(root.left)
            dfs(root.left)
        
        dfs(root)

        nodes.sort()
        return nodes[k-1]