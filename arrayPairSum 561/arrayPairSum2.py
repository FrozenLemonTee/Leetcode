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


def arrayPairSum(nums: List[int]) -> int:
    # 超时
    the_min = []
    if len(nums) == 0:
        return 0
    for i in range(0, len(nums)):
        if not the_min:
            the_min.append(i)
            continue
        if len(the_min) == 1:
            if nums[i] <= nums[the_min[0]]:
                the_min.insert(0, i)
            else:
                the_min.append(i)
        else:
            if nums[i] <= nums[the_min[0]]:
                the_min.pop()
                the_min.insert(0, i)
            elif nums[the_min[0]] < nums[i] <= nums[the_min[1]]:
                the_min[1] = i
            else:
                pass
    result = 0
    result += nums[the_min[0]]
    nums.pop(the_min[0])
    if the_min[0] < the_min[1]:
        nums.pop(the_min[1] - 1)
    else:
        nums.pop(the_min[1])
    return result + arrayPairSum(nums)


if __name__ == "__main__":
    test = [1, 4, 3, 2, 8, 20, 15, 27, 9, 11, -4, -8, -2, -1]
    print(arrayPairSum(test))
