"""
409. 最长回文串

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。


"""


def longestPalindrome(s: str) -> int:
    alpha = {}
    for char in s:
        if char not in alpha.keys():
            alpha.update({char: 1})
        else:
            alpha[char] += 1
    result = 0
    for char in alpha.keys():
        result += (alpha[char] // 2) * 2
        alpha[char] %= 2
    for char in alpha.keys():
        if alpha[char]:
            result += 1
            break
    return result


if __name__ == "__main__":
    test = "dDaebEEecbBcaccAddA"
    print(longestPalindrome(test))