from DSAA.data_structure.basic.LeetcodeNode import TreeNode
from Leetcode.isSubtree_572.isSubtree2 import isSubtree

if __name__ == "__main__":
    test2 = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(1, None, TreeNode(2))))))
    test1 = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(1, test2)))))
    print(isSubtree(test1, test2))  # True
    test3 = TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, TreeNode(2)))))
    test4 = TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, test3))))
    print(isSubtree(test3, test4))  # False
    test5 = TreeNode(-6, TreeNode(-9, None, TreeNode(-8, None, TreeNode(-7))), TreeNode(-3, TreeNode(-4), TreeNode(1, TreeNode(0), TreeNode(5, TreeNode(2)))))
    test6 = TreeNode(-6, TreeNode(-9, None, TreeNode(-8, None, TreeNode(-7))), TreeNode(-3, TreeNode(-4), TreeNode(1)))
    print(isSubtree(test5, test6))  # False
