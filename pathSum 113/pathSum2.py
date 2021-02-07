"""
113. 路径总和 II

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""

import collections

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def pathSum(root: TreeNode, summary: int) -> List[List[int]]:
    res = []
    if root:
        node_list = collections.deque([[root, [root.val], root.val]])
        while node_list:
            tmp = node_list.popleft()
            node, path, cur_sum = tmp[0], tmp[1], tmp[2]
            if not node.left and not node.right and cur_sum == summary:
                res.append(path)
            if node.left:
                node_list.append([node.left, path + [node.left.val], cur_sum + node.left.val])
            if node.right:
                node_list.append([node.right, path + [node.right.val], cur_sum + node.right.val])

    return res


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(1)))
    print(pathSum(test, 3))
