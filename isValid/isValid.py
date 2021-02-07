"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true


"""


def isValid(s: str) -> bool:
    def isRightBracket(c: str):
        if c == ")" or c == "]" or c == "}":
            return True
        else:
            return False

    def isCouple(c1: str, c2: str):
        string = "{0}{1}".format(c1, c2)
        if string == "()" or string == "[]" or string == "{}":
            return True
        else:
            return False

    tmp = []
    i = 0
    for j in range(0, 2):
        if j > len(s) - 1:
            break
        tmp.append(s[i])
        j += 1
        i = j
    while len(tmp) > 0:
        if len(tmp) >= 2:
            if isRightBracket(tmp[-1]):
                if isCouple(tmp[-2], tmp[-1]):
                    tmp.pop()
                    tmp.pop()
                else:
                    return False
            elif i > len(s) - 1:
                return False
        else:
            if i > len(s) - 1:
                return False
        if i <= len(s) - 1:
            i += 1
            tmp.append(s[i - 1])
    return True


if __name__ == "__main__":
    test = "([)]"
    print(isValid(test))  # False
    test2 = "([]()){}"
    print(isValid(test2))  # True
    test3 = "(("
    print(isValid(test3))  # False
    test4 = "))"
    print(isValid(test4))  # False
    test5 = ")"
    print(isValid(test5))  # False
    test6 = "({[{()}]})"
    print(isValid(test6))  # True
    test7 = "()"
    print(isValid(test7))  # True
