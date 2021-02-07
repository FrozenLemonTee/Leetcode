"""
515. 在每个树行中找最大值

您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def largestValues(root: TreeNode) -> List[int]:
    res = []

    def recursion(node: TreeNode, layers: int) -> None:
        if node:
            if len(res) < layers:
                res.append(node.val)
            else:
                res[layers - 1] = max(res[layers - 1], node.val)
            if node.left:
                recursion(node.left, layers + 1)
            if node.right:
                recursion(node.right, layers + 1)

    recursion(root, 1)
    return res


if __name__ == "__main__":
    test = TreeNode(0, TreeNode(-1))
    print(largestValues(test))
