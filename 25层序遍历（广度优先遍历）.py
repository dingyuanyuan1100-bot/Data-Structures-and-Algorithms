"""
给你二叉树的根节点 root,返回其节点值的层序遍历。(即逐层地,从左到右访问所有节点)。
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#广度优先，队列实现
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []#存放结果
        if root is None:
            return res
        queue = deque([root])#队列用来存放戴检索节点
        while queue:
            cur_res = []#转门存该节点的值
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                cur_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_res)
        return res 