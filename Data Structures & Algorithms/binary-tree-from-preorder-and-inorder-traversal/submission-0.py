class Solution:
    def buildTree(
        self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        inorder_index = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            split = inorder_index[root_value]

            root.left = build(left, split - 1)
            root.right = build(split + 1, right)

            return root

        return build(0, len(inorder) - 1)