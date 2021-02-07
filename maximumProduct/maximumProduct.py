"""
628. 三个数的最大乘积

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6

示例 2:

输入: [1,2,3,4]
输出: 24

注意:

    给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
    输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


"""
from typing import List


def maximumProduct(nums: List[int]) -> int:
    tmp = nums.copy()
    tmp.sort()
    # if tmp[len(tmp) - 1] * tmp[len(tmp) - 2] * tmp[len(tmp) - 3] > tmp[0] * tmp[1] * tmp[len(tmp) - 1]:
    #     return tmp[len(tmp) - 1] * tmp[len(tmp) - 2] * tmp[len(tmp) - 3]
    # else:
    #     return tmp[0] * tmp[1] * tmp[len(tmp) - 1]
    return max(tmp[0] * tmp[1] * tmp[len(tmp) - 1], tmp[len(tmp) - 1] * tmp[len(tmp) - 2] * tmp[len(tmp) - 3])
