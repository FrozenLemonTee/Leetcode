"""
367. 有效的完全平方数

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True

示例 2：

输入：14
输出：False
"""


def isPerfectSquare(num: int) -> bool:
    low = 1
    high = num
    mid = (low + high) // 2
    while low <= high:
        if mid * mid == num:
            return True
        elif mid * mid > num:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
    return False


if __name__ == "__main__":
    print(isPerfectSquare(13))
    print(isPerfectSquare(16))
    print(isPerfectSquare(25))
    print(isPerfectSquare(26))
