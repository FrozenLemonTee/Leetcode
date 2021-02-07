"""
572. 另一个树的子树

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2

给定的树 t：

   4
  / \
 1   2

返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0

给定的树 t：

   4
  / \
 1   2

返回 false。

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from Leetcode.isSameTree_100.isSameTree import isSameTree


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    def recursion(node_s: TreeNode) -> bool:
        if not isSameTree(node_s, t):
            left = right = False
            if node_s.left:
                left = recursion(node_s.left)
            if node_s.right:
                right = recursion(node_s.right)
            return left or right
        else:
            return True

    return recursion(s)
