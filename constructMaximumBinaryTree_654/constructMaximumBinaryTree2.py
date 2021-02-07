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


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    def constructChild(left_index: int, right_index: int) -> TreeNode or None:
        if left_index != right_index:
            index = cur = left_index
            while cur < right_index:
                if nums[cur] > nums[index]:
                    index = cur
                cur += 1
            result = TreeNode(nums[index])
            result.left = constructChild(left_index, index)
            result.right = constructChild(index + 1, right_index)
            return result

    return constructChild(0, len(nums))


if __name__ == "__main__":
    print(constructMaximumBinaryTree([3, 2, 7, 6, 0, 5]))
