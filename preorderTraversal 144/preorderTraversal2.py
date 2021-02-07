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
    def returnChildren(pointer: TreeNode) -> List[int]:
        res = []
        if pointer:
            if pointer.left:
                res.append(pointer.left)
            if pointer.right:
                res.append(pointer.right)
        return res

    result = []
    if root:
        node_list = [root]
        while node_list:
            result.append(node_list[0].val)
            tmp = returnChildren(node_list[0])
            node_list.pop(0)
            node_list = tmp + node_list
    return result
