"""
485. 最大连续1的个数

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：

    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。


"""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """遍历统计法"""
    maxi = 0
    cur = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            cur += 1
        else:
            if maxi < cur:
                maxi = cur
            cur = 0
    if maxi < cur:
        maxi = cur
    return maxi


if __name__ == "__main__":
    test1 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    test2 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    test3 = [1, 0, 1, 1]
    print(findMaxConsecutiveOnes(test1))
    print(findMaxConsecutiveOnes(test2))
    print(findMaxConsecutiveOnes(test3))
