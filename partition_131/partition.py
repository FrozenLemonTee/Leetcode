"""
131. 分割回文串

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    def backTracking(left: int) -> None:
        if left >= len(s):
            res.append(path.copy())
            return
        for m in range(left, len(s)):
            if palindrome[left][m]:
                path.append(s[left: m + 1])
            else:
                continue
            backTracking(m + 1)
            path.pop()

    def palindromeFill(left: int, right: int) -> None:
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            palindrome[left][right] = True
            left -= 1
            right += 1

    palindrome = [[False] * len(s) for _ in range(0, len(s))]
    res = []
    path = []
    for i in range(0, len(s)):
        palindromeFill(i, i)
        palindromeFill(i, i + 1)

    backTracking(0)
    return res


if __name__ == "__main__":
    print(partition("aaa"))
    print(partition("bbab"))
