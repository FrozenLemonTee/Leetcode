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

from collections import deque


def findBottomLeftValue(root: TreeNode) -> int:
    res = [root, 1]
    node_list = deque([res])
    while node_list:
        if node_list[0][1] > res[1]:
            res = node_list[0]
        if node_list[0][0].left:
            node_list.append([node_list[0][0].left, node_list[0][1] + 1])
        if node_list[0][0].right:
            node_list.append([node_list[0][0].right, node_list[0][1] + 1])
        node_list.popleft()
    return res[0].val
