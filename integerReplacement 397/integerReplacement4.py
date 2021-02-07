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
    """递归法优化：用哈希表记录"""
    visited = {}

    def countSum(m: int) -> int:
        if m in visited.keys():
            return visited[m]
        elif m == 1:
            visited.update({1: 0})
            return 0
        elif m % 2 == 0:
            res = countSum(m // 2) + 1
            visited.update({m: res})
            return res
        else:
            minus = countSum(m - 1) + 1
            plus = countSum(m + 1) + 1
            if minus <= plus:
                res = minus
            else:
                res = plus
            visited.update({m: res})
            return res

    return countSum(n)


if __name__ == "__main__":
    print(integerReplacement(15))
