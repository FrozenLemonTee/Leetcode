"""
451. 根据字符出现频率排序

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""


def frequencySort(s: str) -> str:
    freq = {}
    for c in s:
        if c not in freq.keys():
            freq.update({c: 1})
        else:
            freq[c] += 1
    freq = sorted(freq.items(), key=lambda items: items[1], reverse=True)
    ans = ""
    print(freq)
    for item in freq:
        for i in range(0, int(item[1])):
            ans += item[0]
    return ans


if __name__ == "__main__":
    print(frequencySort("eerfaavqAKKcadggaqwrqw"))
