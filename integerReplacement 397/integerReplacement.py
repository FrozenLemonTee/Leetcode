"""
397. 整数替换

给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1

示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
"""


def integerReplacement(n: int) -> int:
    """递归法"""
    def countSum(m: int) -> int:
        if m == 1:
            return 0
        elif m % 2 == 0:
            return countSum(m // 2) + 1
        else:
            return min(countSum(m - 1) + 1, countSum(m + 1) + 1)

    return countSum(n)


if __name__ == "__main__":
    for i in range(1, 201):
        print("integerReplacement({0}) = {1}".format(i, integerReplacement(i)))
