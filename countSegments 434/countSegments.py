"""
434. 字符串中的单词数

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


"""


def countSegments(s: str) -> int:
    s = s.rstrip()
    result = 0
    flag = 0
    for c in s:
        if c == " ":
            if flag == 1:
                result += 1
                flag = 0
            continue
        else:
            flag = 1
    if flag == 1:
        result += 1
    return result


if __name__ == "__main__":
    test = ", , , ,        a, eaefa"
    print(countSegments(test))
