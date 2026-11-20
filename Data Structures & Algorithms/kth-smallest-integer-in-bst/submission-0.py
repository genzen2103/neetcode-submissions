class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal k

            if node is None:
                return None

            result = inorder(node.left)
            if result is not None:
                return result

            k -= 1
            if k == 0:
                return node.val

            return inorder(node.right)

        return inorder(root)