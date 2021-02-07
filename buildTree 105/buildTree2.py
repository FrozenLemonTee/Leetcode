"""
105. 从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


"""
from typing import List

# Definition for a Node.
from DSAA.data_structure.basic.LeetcodeNode import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode or None:
    def buildChildTree(pre_l: int, pre_r: int, ino_l: int, ino_r: int) -> TreeNode or None:
        root = None
        if pre_l <= pre_r:
            root = TreeNode(preorder[pre_l])
            index = dic[preorder[pre_l]]
            size_l = index - ino_l
            root.left = buildChildTree(pre_l + 1, pre_l + size_l, ino_l, ino_l + size_l - 1)
            root.right = buildChildTree(pre_l + 1 + size_l, pre_r, ino_l + size_l + 1, ino_r)
        return root

    dic = {}
    length = len(preorder)
    for i in range(0, length):
        dic.update({inorder[i]: i})

    return buildChildTree(0, length - 1, 0, length - 1)


if __name__ == "__main__":
    print(buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))
