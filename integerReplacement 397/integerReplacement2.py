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
from typing import List


def integerReplacement(n: int) -> int:
    """迭代法"""
    def exactDivision(m: int) -> List[int]:
        count = 0
        while m % 2 == 0:
            m = m // 2
            count += 1
        return [count, m]

    total = 0
    while n > 1:
        if n % 2 == 0:
            tmp = exactDivision(n)
            total += tmp[0]
            n = tmp[1]
        else:
            plus = exactDivision(n + 1)
            minus = exactDivision(n - 1)
            total += 1
            # 哪种除二次数更多就选哪种
            if plus[0] > minus[0] and n != 3:
                total += plus[0]
                n = plus[1]
            else:
                total += minus[0]
                n = minus[1]
    return total


if __name__ == "__main__":
    for i in range(1, 11):
        print("integerReplacement({0}) = {1}".format(i, integerReplacement(i)))
    print(integerReplacement(5))
