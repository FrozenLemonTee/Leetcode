"""
125. 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false
"""


def isPalindrome(s: str) -> bool:
    if s:
        front = 0
        last = len(s) - 1
        while front < last:
            while not s[front].isalnum():
                front += 1
                if front > len(s) - 1:
                    return True
            while not s[last].isalnum():
                last -= 1
                if last < 0:
                    return True
            if front >= last:
                break
            print(s[front].isalpha(), "==", s[last].isalpha(), s[front], s[last])
            if s[front].isalpha() and s[last].isalpha():
                if s[front].lower() != s[last].lower():
                    return False
            elif s[front].isdigit() and s[last].isdigit():
                if s[front] != s[last]:
                    return False
            else:
                return False
            front += 1
            last -= 1
    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("0P"))
