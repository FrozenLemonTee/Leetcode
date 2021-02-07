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

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def minDepth(root: TreeNode) -> int:
    def childrenDepth(pointer: TreeNode) -> int:
        if pointer:
            left = right = 0
            if pointer.left:
                left = childrenDepth(pointer.left)
            if pointer.right:
                right = childrenDepth(pointer.right)
            if left == 0 or right == 0:
                return 1 + max(left, right)
            else:
                return 1 + min(left, right)
        return 0

    return childrenDepth(root)


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(2))
    print(minDepth(test))  # 2
    test2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(minDepth(test2))  # 3
