"""
540. 有序数组中的单一元素

给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10

注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
"""
from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    """暴力解法（未通过：长数据输入后输出的结果有误，原因未知）"""
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 3 and nums[0] == nums[1]:
        return nums[2]
    elif nums[0] != nums[1]:
        return nums[0]
    for i in range(0, len(nums) // 2 + 3, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
        if 2 * (i + 1) > len(nums) - 1:
            break
    return nums[len(nums) - 1]


if __name__ == "__main__":
    test1 = [1, 1, 2, 2, 3]
    print(singleNonDuplicate(test1))
    test2 = [3, 3, 7, 7, 10, 11, 11]
    print(singleNonDuplicate(test2))
    test3 = [1, 1, 3, 3, 4, 4, 8, 8, 10, 10, 12, 12, 13, 13, 15]
    print(singleNonDuplicate(test3))
    test4 = [1]
    print(singleNonDuplicate(test4))
    test5 = [1, 1, 2]
    print(singleNonDuplicate(test5))
