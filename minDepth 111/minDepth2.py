"""
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回它的最小深度  2
"""

import collections

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    node_list = collections.deque([[root, 1]])
    while node_list:
        node, depth = node_list.popleft()

        # 层次遍历中最先遍历到的叶子节点一定有到根节点最短的路径
        if not node.left and not node.right:
            return depth
        if node.left:
            node_list.extend([[node.left, depth + 1]])
        if node.right:
            node_list.extend([[node.right, depth + 1]])

    return 0


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(3))
    print(minDepth(test))  # 2
    test2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(minDepth(test2))  # 3
