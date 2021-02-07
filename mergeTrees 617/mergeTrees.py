"""
617. 合并二叉树

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1:                    Tree 2:
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

注意: 合并必须从两个树的根节点开始。

"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    def recurseMerge(nodes: List[TreeNode]) -> None or TreeNode:
        if not nodes[0] and not nodes[1]:
            return
        result = TreeNode()
        left = []
        right = []
        if nodes[0]:
            result.val += nodes[0].val
            left.append(nodes[0].left)
            right.append(nodes[0].right)
        else:
            left.append(None)
            right.append(None)
        if nodes[1]:
            result.val += nodes[1].val
            left.append(nodes[1].left)
            right.append(nodes[1].right)
        else:
            left.append(None)
            right.append(None)
        result.left = recurseMerge(left)
        result.right = recurseMerge(right)
        return result

    return recurseMerge([t1, t2])


if __name__ == "__main__":
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(mergeTrees(tree1, tree2))
