from tkinter.filedialog import Open
from typing import Optional
"""
给你二叉树的根节点 root,返回它节点值的 前序 遍历。
示例1:
输入:root=f[1,null,2,3]
输出:[1,2,3]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归写法(前序遍历)
class Solution1:
    def preorderTraversal(self,root:Optional[TreeNode])->Optional[list[int]]:
        result = []
        def f(node:TreeNode)->Optional[list[int]]:
            if node is None:
                return
            result.append(node.val)
            f(node.left)
            f(node.right)
            return
        f(root)
        return result

#递归写法（后序遍历）
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode])->Optional[list[int]]:
        result = []
        def f(node:TreeNode)->Optional[list[int]]:
            if node is None:
                return
            f(node.left)
            f(node.right)
            result.append(node.val)
            return
        f(root)
        return result

#栈迭代(前序写法)
class Solution3:
    def preorderTraversal(self, root: Optional[TreeNode])->Optional[list[int]]:
        if not root:
            return
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

