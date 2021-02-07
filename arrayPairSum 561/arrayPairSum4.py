"""
561. 数组拆分 I

给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).

提示:

    n 是正整数,范围在 [1, 10000].
    数组中的元素范围在 [-10000, 10000].


"""
from typing import List
import math


def arrayPairSum(nums: List[int]) -> int:
    sort = [0] * 20001
    flag = 0
    result = 0
    for i in range(0, len(nums)):
        sort[nums[i] + 10000] += 1
    for j in range(0, len(sort)):
        if flag and sort[j]:
            sort[j] -= 1
            flag = 0
        if sort[j] > 0:
            result += math.ceil(sort[j] / 2) * (j - 10000)
            if sort[j] % 2 != 0:
                flag = 1
            else:
                flag = 0
    return result


if __name__ == "__main__":
    test = [1, 4, 3, 2, 8, 20, 15, 27, 9, 11, -4, -8, -2, -1]
    print(arrayPairSum(test))
    test2 = [1, 1, 2, 3]
    print(arrayPairSum(test2))
