"""
680. 验证回文字符串 Ⅱ

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True

示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:

    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


"""


def validPalindrome(s: str) -> bool:
    pos = [0, len(s) - 1]
    i = 0
    j = len(s) - 1
    flag = 0
    left_flag = right_flag = 0
    while i < j:
        if s[i] != s[j] and flag == 0:
            flag = 1
            pos = [i, j]
            if s[i + 1] == s[j]:
                left_flag = 1
                i += 1
            elif s[i] == s[j - 1]:
                right_flag = 1
                j -= 1
            else:
                return False
            continue
        if s[i] != s[j]:
            if flag == 1:
                if left_flag == 1 and right_flag == 1:
                    return False
                else:
                    i = pos[0]
                    j = pos[1]
                    if left_flag == 0:
                        i += 1
                        left_flag = 1
                    else:
                        j -= 1
                        right_flag = 1
                    continue
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    test = "aebttbea"
    print(validPalindrome(test))  # True
    test2 = "aebttbmea"
    print(validPalindrome(test2))  # True
    test3 = "afebttbmea"
    print(validPalindrome(test3))  # False
    test4 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(validPalindrome(test4))  # True
