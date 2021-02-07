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
    def recursion(pre: List[int], ino: List[int]) -> TreeNode or None:
        root = None
        if pre:
            root = TreeNode(pre[0])
            index = 0
            #  每次都线性查找
            while index <= len(ino) - 1:
                if ino[index] != pre[0]:
                    index += 1
                else:
                    break
            root.left = recursion(pre[1:1 + index], ino[:index])
            root.right = recursion(pre[1 + index:], ino[index + 1:])
        return root

    return recursion(preorder, inorder)


if __name__ == "__main__":
    print(buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))
