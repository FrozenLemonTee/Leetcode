"""
590. N叉树的后序遍历

给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :

返回其后序遍历: [5,6,3,2,4,1].



说明: 递归法很简单，你可以使用迭代法完成此题吗
"""

import collections

# Definition for a Node.
from DSAA.data_structure.basic.LeetcodeNode import KTreeNode

from typing import List


def postorder(root: KTreeNode) -> List[int]:
    res = []
    if root:
        node_list = collections.deque([[root, 0]])
        while node_list:
            if node_list[0][1] == 0:
                node_list[0][1] = 1
                if node_list[0][0].children:
                    tmp = collections.deque([])
                    for child in node_list[0][0].children:
                        tmp.append([child, 0])
                    node_list = tmp + node_list
            else:
                res.append(node_list.popleft()[0].val)

    return res


if __name__ == "__main__":
    test = KTreeNode(1, [KTreeNode(3, [KTreeNode(5), KTreeNode(6)]), KTreeNode(2), KTreeNode(4)])
    print(postorder(test))
