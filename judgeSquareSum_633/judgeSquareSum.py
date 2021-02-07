"""
633. 平方数之和

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。



示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：

输入：c = 3
输出：false

示例 3：

输入：c = 4
输出：true

示例 4：

输入：c = 2
输出：true

示例 5：

输入：c = 1
输出：true



提示：

    0 <= c <= 231 - 1
"""
from Leetcode.isPerfectSquare_367.isPerfectSquare import isPerfectSquare


def judgeSquareSum(c: int) -> bool:
    low = 1
    high = c
    mid = (low + high) // 2
    while ((low + high) // 2) ** 2 >= c:
        if ((low + high) // 2) ** 2 == c:
            return True
        high = mid - 1
        mid = (low + high) // 2
    for i in range(0, high + 1):
        if isPerfectSquare(c - i ** 2):
            return True
    return False


if __name__ == "__main__":
    print(judgeSquareSum(5))
    print(judgeSquareSum(4))
    print(judgeSquareSum(101))
    print(judgeSquareSum(113))
    print(judgeSquareSum(9))
