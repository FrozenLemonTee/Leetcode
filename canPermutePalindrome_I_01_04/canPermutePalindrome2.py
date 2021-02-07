"""
面试题 01.04. 回文排列

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。



示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""


def canPermutePalindrome(s: str) -> bool:
    dic = {}
    for c in s:
        if c not in dic.keys():
            dic.update({c: 1})
        else:
            dic[c] += 1
    flag = 0
    for mem in dic.keys():
        if dic[mem] % 2 != 0:
            if flag == 0:
                flag = 1
            else:
                return False
    return True


if __name__ == "__main__":
    print(canPermutePalindrome("tactcoa"))
