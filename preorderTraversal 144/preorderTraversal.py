"""
144. 二叉树的前序遍历

给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

from typing import List

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def preorderTraversal(root: TreeNode) -> List[int]:
    def traverse(pointer: TreeNode):
        result = []
        if pointer:
            result.append(pointer.val)
            if pointer.left:
                result += traverse(pointer.left)
            if pointer.right:
                result += traverse(pointer.right)
        return result

    return traverse(root)
