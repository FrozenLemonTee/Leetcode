"""
94. 二叉树的中序遍历

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def postorderTraversal(root: TreeNode) -> List[int]:
    result = []
    if root:
        node_list = [root]
        visited = [0]
        while node_list:
            if visited[0] == 0:
                visited[0] = 1
                index = 0
                if node_list[index].left:
                    node_list.insert(0, node_list[index].left)
                    visited.insert(0, 0)
                    index = 1
                if node_list[index].right:
                    if index == 0:
                        node_list.insert(1, node_list[index].right)
                        visited.insert(1, 0)
                    else:
                        node_list.insert(2, node_list[index].right)
                        visited.insert(2, 0)
            else:
                result.append(node_list[0].val)
                node_list.pop(0)
                visited.pop(0)
    return result


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(postorderTraversal(test))  # [4,2,5,1,6,3,7]
