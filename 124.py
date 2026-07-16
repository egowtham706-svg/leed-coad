

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through the current node
            self.max_sum = max(self.max_sum, node.val + left + right)

            # Return the maximum gain to the parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
