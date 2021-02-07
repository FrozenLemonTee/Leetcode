"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false


"""

# Definition for a binary tree node.
from typing import List

from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def returnChild(pointer: TreeNode) -> List[TreeNode]:
        if not pointer:
            return []
        result = []
        if pointer.left:
            result.append(pointer.left)
        else:
            result.append(None)
        if pointer.right:
            result.append(pointer.right)
        else:
            result.append(None)
        return result
    if not p and not q:
        return True
    if not p or not q:
        return False
    node_list1 = []
    node_list2 = []
    node_pointer1 = p
    node_pointer2 = q
    node_list1.append(node_pointer1)
    node_list2.append(node_pointer2)
    while True:
        if not node_pointer1 and not node_pointer2:
            node_list1.pop(0)
            node_list2.pop(0)
            if not node_list1 and not node_list2:
                break
            node_pointer1 = node_list1[0]
            node_pointer2 = node_list2[0]
            continue
        if not node_pointer1 or not node_pointer2:
            return False
        if len(node_list1) != len(node_list2) or node_list1[0].val != node_list2[0].val:
            return False
        else:
            node_list1 += returnChild(node_pointer1)
            node_list2 += returnChild(node_pointer2)
            node_list1.pop(0)
            node_list2.pop(0)
            if not node_list1 and not node_list2:
                break
            node_pointer1 = node_list1[0]
            node_pointer2 = node_list2[0]
    return True


if __name__ == "__main__":
    tree1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(isSameTree(tree1, tree2))
