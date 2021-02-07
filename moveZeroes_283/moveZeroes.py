"""
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""
from typing import List


def moveZeroes(nums: List[int]) -> None:
    if nums:
        pre = 0
        last = len(nums) - 1
        while pre < last:
            if nums[last] != 0 and nums[pre] == 0:
                nums.append(nums.pop(pre))
                if pre != 0:
                    pre -= 1
            if nums[last] == 0:
                last -= 1
            if nums[pre] != 0:
                pre += 1


if __name__ == "__main__":
    test = [0, 1, 0, 3, 12]
    moveZeroes(test)
    print(test)
    test2 = [0, 0, 0, 0, 0, 1]
    moveZeroes(test2)
    print(test2)
