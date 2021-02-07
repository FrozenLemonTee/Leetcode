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
    palindrome = [[False] * len(s) for _ in range(0, len(s))]

    def palindromeFill(left: int, right: int) -> None:
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            palindrome[left][right] = True
            left -= 1
            right += 1

    for i in range(0, len(s)):
        palindromeFill(i, i)
        palindromeFill(i, i + 1)

    dp = [1] * (len(s) + 1)
    index = 0
    for j in range(0, len(dp)):
        if j == 0:
            dp[j] = 0
            continue
        for k in range(0, j):
            if palindrome[k][j - 1]:
                dp[j] = max(dp[j], j - k)
        if dp[index] < dp[j]:
            index = j

    return s[index - dp[index]: index]


if __name__ == "__main__":
    print(longestPalindrome("babad"))
