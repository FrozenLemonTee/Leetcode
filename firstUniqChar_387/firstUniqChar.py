"""
387. 字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。



示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。
"""


def firstUniqChar(s: str) -> int:
    alpha = {}
    for i in range(0, len(s)):
        if s[i] not in alpha.keys():
            alpha.update({s[i]: [i]})
        else:
            alpha[s[i]].append(i)
    ans = []
    for k in alpha.keys():
        if len(alpha[k]) == 1:
            ans.extend(alpha[k])
    return min(ans) if ans else -1


if __name__ == "__main__":
    print(firstUniqChar("te"))
