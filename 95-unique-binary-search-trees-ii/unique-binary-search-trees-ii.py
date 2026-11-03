# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):

        def build(start, end):
            if start > end:
                return [None]

            result = []

            for i in range(start, end + 1):
                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return build(1, n)
