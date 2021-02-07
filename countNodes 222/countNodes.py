"""
222. 完全二叉树的节点个数

给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6


"""

# Definition for a binary tree node.
from typing import List

from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def countNodes(root: TreeNode) -> int:
    def returnChildren(pointer: TreeNode) -> List[TreeNode]:
        if not pointer:
            return []
        else:
            result = []
            if pointer.left:
                result.append(pointer.left)
            # else:
            #     result.append(None)
            if pointer.right:
                result.append(pointer.right)
            # else:
            #     result.append(None)
        return result
    count = 0
    node_list = [root]
    while node_list:
        node_pointer = node_list[0]
        node_list += returnChildren(node_pointer)
        if node_pointer:
            count += 1
        node_list.pop(0)
    return count


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    print(countNodes(tree))
