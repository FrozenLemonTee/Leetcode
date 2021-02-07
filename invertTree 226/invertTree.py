"""
226. 翻转二叉树

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def invertTree(root: TreeNode) -> TreeNode:
    def returnChildren(pointer: TreeNode):
        result = []
        if pointer:
            if pointer.left:
                result.append(pointer.left)
            if pointer.right:
                result.append(pointer.right)
        return result

    if root:
        node_list = [root]
        while node_list:
            node_list += returnChildren(node_list[0])
            node_list[0].left, node_list[0].right = node_list[0].right, node_list[0].left
            node_list.pop(0)
    return root


if __name__ == "__main__":
    test = TreeNode(1)
    print(invertTree(test))
