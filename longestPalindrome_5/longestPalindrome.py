"""
5. 最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"
"""


def longestPalindrome(s: str) -> str:
    def extendStr(left: int, right: int) -> (int, int):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    res = 0, 0
    for index in range(0, len(s)):
        start1, end1 = extendStr(index, index)
        start2, end2 = extendStr(index, index + 1)
        if end1 - start1 > res[1] - res[0]:
            res = start1, end1
        if end2 - start2 > res[1] - res[0]:
            res = start2, end2
    return s[res[0]: res[1] + 1]


if __name__ == "__main__":
    print(longestPalindrome("cbbd"))  # bb
    print(longestPalindrome("babad"))  # bab (aba)
    print(longestPalindrome("bb"))
    print(longestPalindrome("cccc"))
    print(longestPalindrome("csdeeseeaeeeeeee"))
    print(longestPalindrome("cccd"))
