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
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not (p and q):
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    tree1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(isSameTree(tree1, tree2))
