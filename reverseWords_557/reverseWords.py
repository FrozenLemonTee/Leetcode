"""
557. 反转字符串中的单词 III

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。



示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"



提示：

    在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格
"""


def reverseWords(s: str) -> str:
    tmp = s.split(" ")
    res = ""
    for i in range(0, len(tmp)):
        w = list(tmp[i])
        for j in range(0, (len(w) - 1) // 2 + 1):
            w[j], w[-(j+1)] = w[-(j+1)], w[j]
        res += ("".join(c for c in w) + " ")
    return res.strip(" ")


if __name__ == "__main__":
    print(reverseWords("Let's take LeetCode contest"))
