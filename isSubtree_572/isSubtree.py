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
from typing import List

from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from collections import deque


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    # 改正
    def isEqual(node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 and not node2:
            return True
        if not (node1 and node2):
            return False
        if bool(node1.left) ^ bool(node2.left) or bool(node1.right) ^ bool(node2.right):
            return False
        if node1.val == node2.val:
            if node1.left and node2.left:
                left = bool(node1.left.val == node2.left.val)
            else:
                left = True
            if node1.right and node2.right:
                right = bool(node1.right.val == node2.right.val)
            else:
                right = True
            return left and right
        else:
            return False

    def getChildNode(node: List) -> List or None:
        if node[1] == 0:
            node[1] = 1
            if node[0].left:
                return [node[0].left, 0, 0]
            else:
                return [None, 1, 1]
        if node[2] == 0:
            node[2] = 1
            if node[0].right:
                return [node[0].right, 0, 0]
            else:
                return [None, 1, 1]

    if not s and not t:
        return True
    if not (s and t):
        return False

    stack_s = deque([[s, 0, 0]])
    stack_t = deque([[t, 0, 0]])
    while stack_s and stack_t:
        cur1 = stack_s[-1]
        cur2 = stack_t[-1]
        tmp_s = getChildNode(cur1)
        tmp_t = getChildNode(cur2)
        if cur1[1] == 1 and cur1[2] == 1:
            stack_s.pop()
        if tmp_s:
            stack_s.append(tmp_s)
        if cur2[1] == 1 and cur2[2] == 1:
            stack_t.pop()
        if tmp_t:
            stack_t.append(tmp_t)
        if not isEqual(cur1[0], cur2[0]):
            if len(stack_s) >= 2:
                stack_s = deque([stack_s[0], [stack_s[1][0], 0, 0]])
            stack_t = deque([[t, 0, 0]])
    return not stack_t
