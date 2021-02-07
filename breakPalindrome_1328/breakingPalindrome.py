"""
1328. 破坏回文串

给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。

请你返回结果字符串。如果无法做到，则返回一个空串。



示例 1：

输入：palindrome = "abccba"
输出："aaccba"

示例 2：

输入：palindrome = "a"
输出：""



提示：

    1 <= palindrome.length <= 1000
    palindrome 只包含小写英文字母。
"""
import math


def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) < 2:
        return ""
    arr = list(palindrome)
    for i in range(0, len(arr)):
        if arr[i] != "a" and i != math.ceil((len(palindrome) + 1) / 2) - 1:
            arr[i] = "a"
            return "".join(arr)
    for j in range(-1, -len(palindrome), -1):
        if arr[j] != "b":
            arr[j] = "b"
            return "".join(arr)
    return ""


if __name__ == "__main__":
    print(breakPalindrome("abba"))
