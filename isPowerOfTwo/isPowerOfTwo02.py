"""
231. 2的幂

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1

示例 2:

输入: 16
输出: true
解释: 24 = 16

示例 3:

输入: 218
输出: false


"""


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    total = i = 0
    while True:
        if total == n:
            return True
        elif total > n:
            return False
        else:
            total = 2 ** i
            i += 1


if __name__ == "__main__":
    print(isPowerOfTwo(536870912))