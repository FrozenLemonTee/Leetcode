"""
977. 有序数组的平方

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。



示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]



提示：

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A 已按非递减顺序排序。
"""
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(0, len(nums)):
        if nums[i] < 0:
            nums[i] *= -1
        else:
            break
    nums.sort()
    res = []
    for i in range(0, len(nums)):
        res.append(nums[i] ** 2)
    return res


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))
