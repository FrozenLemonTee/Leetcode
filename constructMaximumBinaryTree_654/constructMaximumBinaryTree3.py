"""
654. 最大二叉树

给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

    二叉树的根是数组中的最大元素。
    左子树是通过数组中最大值左边部分构造出的最大二叉树。
    右子树是通过数组中最大值右边部分构造出的最大二叉树。

通过给定的数组构建最大二叉树，并且输出这个树的根节点。



示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1



提示：

    给定的数组的大小在 [1, 1000] 之间。
"""

# Definition for a binary tree node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode

from typing import List


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode or None:
    if nums:
        nodes = []
        for num in nums:
            cur = TreeNode(num)
            if not nodes or cur.val <= nodes[-1].val:
                nodes.append(cur)
                continue
            while cur.val > nodes[-1].val:
                child = nodes.pop()
                if not nodes or nodes[-1].val > cur.val:
                    cur.left = child
                else:
                    nodes[-1].right = child
                if not nodes:
                    break
            nodes.append(cur)
        while len(nodes) > 1:
            child = nodes.pop()
            nodes[-1].right = child
        return nodes[0]


if __name__ == "__main__":
    print(constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
    print(constructMaximumBinaryTree([1, 4, 5, 8, 6, 7]))
