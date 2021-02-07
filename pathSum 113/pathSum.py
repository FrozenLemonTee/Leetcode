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

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def pathSum(root: TreeNode, summary: int) -> List[List[int]]:
    def childrenSum(pointer: TreeNode, cur_sum: int, cur_path: List[int]) -> List[List[int]]:
        res = []
        if pointer:
            cur = cur_path + [pointer.val]
            #  必须是叶子节点（左右子树为空）
            if cur_sum + pointer.val == summary and not pointer.left and not pointer.right:
                res.append(cur)

            cur_sum += pointer.val
            if pointer.left:
                res += childrenSum(pointer.left, cur_sum, cur)
            if pointer.right:
                res += childrenSum(pointer.right, cur_sum, cur)
        return res

    return childrenSum(root, 0, [])


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(1)))
    print(pathSum(test, 3))
    test2 = TreeNode(1, TreeNode(2))
    print(pathSum(test2, 1))
    test3 = TreeNode(1)
    print(pathSum(test3, 1))
    test4 = TreeNode(-2, None, TreeNode(-3))
    print(pathSum(test4, -5))
