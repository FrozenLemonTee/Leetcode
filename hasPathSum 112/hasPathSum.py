"""
112. 路径总和

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

"""

# Definition for a binary tree node.
from typing import List

from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def hasPathSum(root: TreeNode, summary: int) -> bool:
    def pasteChildren(pointer: TreeNode) -> List[TreeNode]:
        result = []
        if pointer:
            if pointer.left:
                result.append(TreeNode(pointer.val + pointer.left.val, pointer.left.left, pointer.left.right))
            if pointer.right:
                result.append(TreeNode(pointer.val + pointer.right.val, pointer.right.left, pointer.right.right))
        return result

    def isLeafNode(pointer: TreeNode) -> bool:
        if not pointer:
            return False
        if not pointer.left and not pointer.right:
            return True
        else:
            return False

    if not root:
        return False
    else:
        sum_list = []
        node_list = [root]
        node_list += pasteChildren(root)
    while node_list:
        if node_list[0]:
            node_list += pasteChildren(node_list[0])
        if isLeafNode(node_list[0]):
            sum_list.append(node_list[0].val)
        node_list.pop(0)
    dic = set(sum_list)
    if summary in dic:
        return True
    else:
        return False


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(2, TreeNode(5, None, TreeNode(4))), TreeNode(3, TreeNode(2), None))
    print(hasPathSum(test, 6))
