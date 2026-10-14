"""
给定一个二叉树 root,返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def levelOrder(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_result = self.levelOrder(root.left)
        right_result = self.levelOrder(root.right)
        return 1 + max(left_result, right_result)