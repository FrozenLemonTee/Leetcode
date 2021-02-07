"""
331. 验证二叉树的前序序列化

序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true

示例 2:

输入: "1,#"
输出: false

示例 3:

输入: "9,#,#,1"
输出: false

"""

from collections import deque


def isValidSerialization(preorder: str) -> bool:
    preorder = preorder.split(",")
    tmp = deque([])
    index = 0
    for j in range(0, 3):
        if j > len(preorder) - 1:
            break
        tmp.append(preorder[j])
        index = j
    index += 1
    while True:
        if len(tmp) >= 3:
            if tmp[-3].isnumeric() and tmp[-2] == "#" and tmp[-1] == "#":
                for k in range(0, 3):
                    tmp.pop()
                tmp.append("#")
                continue
        if index <= len(preorder) - 1:
            tmp.append(preorder[index])
            index += 1
        elif len(tmp) == 1 and tmp[0] == "#":
            return True
        else:
            return False


if __name__ == "__main__":
    print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(isValidSerialization("1,#"))
    print(isValidSerialization("9,#,#,1"))
