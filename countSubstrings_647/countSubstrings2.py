"""
647. 回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"



提示：

    输入的字符串长度不会超过 1000
"""


def countSubstrings(s: str) -> int:
    dp = [[False] * len(s) for _ in range(0, len(s))]
    res = 0
    for j in range(0, len(s)):
        for i in range(0, j + 1):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                res += 1
                dp[i][j] = True
    return res


if __name__ == "__main__":
    print(countSubstrings("aaa"))
    print(countSubstrings("abc"))
