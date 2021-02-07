"""
49. 字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：

    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = {}
    for word in strs:
        if tuple(sorted(list(word))) not in dic.keys():
            dic.update({tuple(sorted(list(word))): [word]})
        else:
            dic[tuple(sorted(list(word)))].append(word)
    return [mem for mem in dic.values()]


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
