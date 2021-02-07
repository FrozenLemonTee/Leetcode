"""
29. 两数相除

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2



提示：

    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


"""
from typing import List


def divide(dividend: int, divisor: int) -> int:
    def div(dividend1: int, divisor1: int) -> List[int]:
        if abs(dividend1) < abs(divisor1):
            return [0, abs(dividend1)]
        result = abs(divisor1)
        time = 1
        tmp_time = time
        tmp_result = result
        if abs(divisor1) < abs(dividend1):
            while abs(result - abs(dividend1)) > 1:
                while result < abs(dividend1):
                    tmp_time = time
                    tmp_result = result
                    time += time
                    result += result
                if result != abs(dividend1):
                    result = tmp_result
                    tmp = div(abs(dividend1) - result, abs(divisor1))
                    time, result = tmp_time + tmp[0], result + tmp[1]
                else:
                    break
        if abs(result) > abs(dividend1):
            time -= 1
        if (dividend1 > 0 and divisor1 < 0) or (dividend1 < 0 and divisor1 > 0):
            time *= -1
        if time > 2147483647:
            return [2147483647, result]
        if time < -2147483648:
            return [-2147483648, result]
        return [time, result]
    return div(dividend, divisor)[0]


if __name__ == "__main__":
    print(divide(0, 2))  # 0
    print(divide(1, 2))  # 0
    print(divide(2, 2))  # 1
    print(divide(3, 2))  # 1
    print(divide(4, 2))  # 2
    print(divide(7, 2))  # 3
    print(divide(100, 16))  # 6
    print(divide(-10, -3))  # 3
    print(divide(-1000000000, -3))
    print(divide(-2147483648, 1))
