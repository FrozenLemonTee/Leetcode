"""
520. 检测大写字母

给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

    全部字母都是大写，比如"USA"。
    单词中所有字母都不是大写，比如"leetcode"。
    如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。

否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True

示例 2:

输入: "FlaG"
输出: False

注意: 输入是由大写和小写拉丁字母组成的非空单词。

"""


def detectCapitalUse(word: str) -> bool:
    if word[1:]:
        is_lower = bool(not (65 <= ord(word[1]) <= 90))
        for i in range(1, len(word)):
            cur = ord(word[i])
            if not (65 <= cur <= 90) != is_lower:
                return False
        if not (65 <= ord(word[0]) <= 90) and not is_lower:
            return False
    return True


if __name__ == "__main__":
    # True
    print(detectCapitalUse("U"))
    print(detectCapitalUse("u"))
    print(detectCapitalUse("USA"))
    print(detectCapitalUse("usa"))
    print(detectCapitalUse("Usa"))

    print()
    # False
    print(detectCapitalUse("uSA"))
    print(detectCapitalUse("USa"))
    print(detectCapitalUse("UsA"))
    print(detectCapitalUse("usA"))
    print(detectCapitalUse("uSa"))
