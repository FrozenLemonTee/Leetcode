"""
94. 二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def postorderTraversal(root: TreeNode) -> List[int]:
    def traverse(pointer: TreeNode) -> List[int]:
        res = []
        if pointer:
            if pointer.left:
                res += traverse(pointer.left)
            res.append(pointer.val)
            if pointer.right:
                res += traverse(pointer.right)
        return res

    return traverse(root)
