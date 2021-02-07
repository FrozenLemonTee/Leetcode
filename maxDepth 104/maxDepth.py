"""
104. 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3
"""

# Definition for singly-linked list.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def maxDepth(root: TreeNode or None) -> int:
    def recursion(pointer: TreeNode) -> int:
        this = 0
        left = right = 0
        if pointer:
            this = 1
            if pointer.left:
                left = recursion(pointer.left)
            if pointer.right:
                right = recursion(pointer.right)
        return this + max(left, right)
    return recursion(root)


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(2), TreeNode(3))
    print(maxDepth(test))  # 2
    test2 = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(5))), TreeNode(3))
    print(maxDepth(test2))  # 4
    print(maxDepth(None))  # 0
    test3 = TreeNode(5)
    print(maxDepth(test3))  # 1
