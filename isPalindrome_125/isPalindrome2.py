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
        i = 0
        tmp = list(s)
        while i <= len(tmp) - 1:
            if not tmp[i].isalnum():
                tmp.pop(i)
                if i > 0:
                    i -= 1
                continue
            if tmp[i].isalpha():
                tmp[i] = tmp[i].lower()
            i += 1
        m = 0
        n = len(tmp) - 1
        while m < n:
            if tmp[m] != tmp[n]:
                return False
            m += 1
            n -= 1
    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("0P"))
    print(isPalindrome(" "))
    print(isPalindrome(" ])"))
