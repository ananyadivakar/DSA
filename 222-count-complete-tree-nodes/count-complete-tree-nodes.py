# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        left = root
        right = root
        leftHeight = 0
        rightHeight = 0

        while left:
            leftHeight += 1
            left = left.left

        while right:
            rightHeight += 1
            right = right.right

        # Perfect binary tree
        if leftHeight == rightHeight:
            return (1 << leftHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)