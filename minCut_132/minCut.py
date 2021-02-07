"""
132. 分割回文串 II

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""


def minCut(s: str) -> int:
    palindrome = [[False] * len(s) for _ in range(0, len(s))]

    def fillPalindrome(left: int, right: int) -> None:
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            palindrome[left][right] = True
            left -= 1
            right += 1

    for i in range(0, len(s)):
        fillPalindrome(i, i)
        fillPalindrome(i, i + 1)

    dp = [0] * (len(s) + 1)
    for j in range(0, len(dp)):
        if j == 0:
            continue
        dp[j] = j
        for k in range(0, j):
            if palindrome[k][j - 1]:
                dp[j] = min(dp[j], dp[k] + 1)

    return dp[-1] - 1


if __name__ == "__main__":
    print(minCut("abcdefg"))
