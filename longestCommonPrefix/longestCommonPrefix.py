"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。

"""
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    result = ""
    i = j = 0
    while j <= len(strs[0]) - 1:
        cur = strs[0][j]
        while i <= len(strs) - 1:
            if j > len(strs[i]) - 1 or strs[i][j] != cur:
                return result
            i += 1
        i = 0
        result += cur
        j += 1
    return result


if __name__ == "__main__":
    test = ["flower", "flow", "flight"]
    print(longestCommonPrefix(test))
    test2 = ["flo", "flow", "flower"]
    print(longestCommonPrefix(test2))
    test3 = ["aa", "a"]
    print(longestCommonPrefix(test3))
