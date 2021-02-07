"""
513. 找树左下角的值

给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1



示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7



注意: 您可以假设树（即给定的根节点）不为 NULL。

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def findBottomLeftValue(root: TreeNode) -> int:
    def childBottomLeft(node: TreeNode, layers: int) -> List[int]:
        left = [node.val, layers]
        right = [node.val, layers]
        if node.left:
            left = childBottomLeft(node.left, layers + 1)
        if node.right:
            right = childBottomLeft(node.right, layers + 1)
        if left[1] < right[1]:
            return right
        else:
            return left

    return childBottomLeft(root, 0)[0]
