"""
给定一个二叉树,找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为:“对于有根树T的两个节点p、q,最近公共祖先表示为一个节点
x,满足x是p、q的祖先且x的深度尽可能大(一个节点也可以是它自己的祖先)。”
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[
        TreeNode]:
        def dfs(node):
            if not node:
                return False, False, None
            "当前树叉左侧有无p，q,公共祖先"
            l_has_p, l_has_q, l_lca = dfs(node.left)
            "当前树叉右侧有无p,q,公共祖先"
            r_has_p, r_has_q, r_lca = dfs(node.right)

            "当前树叉有无p（左右+本身节点）"
            has_p = l_has_p or r_has_p or node == p
            "当前树叉有无p（左右+本身节点）"
            has_q = l_has_q or r_has_q or node == q

            #如果存在左祖先，返回 有p,q和祖先
            if l_lca:
                return has_p, has_q, l_lca
            #如果存在右祖先，返回 有p,q和祖先
            if r_lca:
                return has_p, has_q, r_lca
            #如果同时有q,p则让lca等于该节点，否则为None
            lca = node if (has_p and has_q) else None
            return has_p, has_q, lca

        _, _, ans = dfs(root)
        return ans