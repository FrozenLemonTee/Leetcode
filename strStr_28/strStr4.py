"""
28. 实现 strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    ph = pn = 0
    while ph <= len(haystack) - len(needle):
        while ph <= len(haystack) - len(needle) and haystack[ph] != needle[pn]:
            ph += 1

        while pn <= len(needle) - 1 and ph <= len(haystack) - 1 and haystack[ph] == needle[pn]:
            ph += 1
            pn += 1

        if pn > len(needle) - 1:
            return ph - len(needle)

        pn -= 1
        ph -= pn
        pn = 0
    return -1
