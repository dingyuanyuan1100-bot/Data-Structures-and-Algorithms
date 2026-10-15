"""
给你一个二叉树的根节点 root,判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下:

    节点的左子树只包含 严格小于 当前节点的数。
    节点的右子树只包含 严格大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode,low = -float("inf") , high = float("inf")) -> bool:
        if root is None:
            return True
        def dfs(node,low = -float("inf"),high = float("inf")):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left,low,high) and dfs(node.right,low,high)

        return dfs(root)