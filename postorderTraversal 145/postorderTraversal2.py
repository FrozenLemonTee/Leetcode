"""
145. 二叉树的后序遍历

给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def postorderTraversal(root: TreeNode) -> List[int]:
    def returnChildren(pointer: TreeNode) -> List[TreeNode]:
        res = []
        if pointer:
            if pointer.left:
                res.append(pointer.left)
            if pointer.right:
                res.append(pointer.right)
        return res

    result = []
    if root:
        node_list = [root]
        visited = [0]
        while node_list:
            if visited[0] == 0:
                tmp = returnChildren(node_list[0])
                visited[0] = 1
                for i in range(0, len(tmp)):
                    visited.insert(0, 0)
                node_list = tmp + node_list
            else:
                result.append(node_list[0].val)
                node_list.pop(0)
                visited.pop(0)
    return result


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(postorderTraversal(test))
