"""
189. 旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。


"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """方案二：中间变量暂时储存"""
    #  超时
    m = abs(k) % len(nums)
    if k > 0:
        nums.append(0)
        for i in range(0, m):
            for j in range(len(nums) - 2, -1, -1):
                nums[j + 1] = nums[j]
            nums[0] = nums[len(nums) - 1]
        nums.pop(-1)
    elif k < 0:
        nums.insert(0, 0)
        for i in range(0, m):
            for j in range(1, len(nums)):
                nums[j - 1] = nums[j]
            nums[len(nums) - 1] = nums[0]
        nums.pop(0)
