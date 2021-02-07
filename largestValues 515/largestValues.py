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

from collections import deque

from typing import List


def largestValues(root: TreeNode) -> List[int]:
    res = []
    if root:
        node_list = deque([[root, 1]])
        layers = 0
        while node_list:
            if node_list[0][0].left:
                node_list.append([node_list[0][0].left, node_list[0][1] + 1])
            if node_list[0][0].right:
                node_list.append([node_list[0][0].right, node_list[0][1] + 1])
            if node_list[0][1] > layers:
                layers = node_list[0][1]
                res.append(node_list[0][0].val)
            else:
                if res[-1] < node_list[0][0].val:
                    res[-1] = node_list[0][0].val
            node_list.popleft()
    return res


if __name__ == "__main__":
    test = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    print(largestValues(test))
